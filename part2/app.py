from fastapi import *
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import Optional
import mysql.connector




import os
sql_password = os.getenv('SQL_PASSWORD')
sql_username = os.getenv('SQL_USER')
db_config = {
    'host': '52.4.229.207',
    'user': sql_username,
    'password': sql_password,
    'database': 'basic_db',
    'port':3306
}
app=FastAPI()
app.mount("/static", StaticFiles(directory='static'), name="static")
headers = {"Content-Type": "application/json; charset=utf-8"}


# uvicorn app:app --reload
# cd /Users/fangsiyu/Desktop/taipei-day-trip




origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000", 
    "http://127.0.0.1:5501",
    "http://52.4.229.207",
    ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,  
    allow_methods=["*"],  
    allow_headers=["*"], 
)
class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/static/") or request.url.path.startswith("/api/attractions") or request.url.path.startswith("/api/attraction") or request.url.path.startswith("/api/mrts"):
            return await call_next(request)
        if request.url.path.startswith("/attraction/") :
            return await call_next(request)
        if request.url.path not in ["/", "/booking", "/thankyou"]:
            return RedirectResponse(url='/')
        return await call_next(request)
app.add_middleware(AuthMiddleware)

@app.get("/api/attractions")
def api_attractions(page: int=Query(..., ge=0), keyword: Optional[str] = None):
    print(f"page = {page}, keyword = {keyword}")
    try:
        mydb = mysql.connector.connect(**db_config, ssl_disabled=True)
        cursor = mydb.cursor(dictionary=True)  # dictionary=True 這個設置就可以不必在69行使用"name":each[1]，而可以直接用
        offset_num = page*12
        keyword_format = f"%{keyword}%"  # 這邊不四多加上"""

        if keyword==None:
            cursor.execute("SELECT SQL_CALC_FOUND_ROWS * FROM processed_data LIMIT 12 OFFSET %s;", (offset_num,)) 
        else:
            cursor.execute("SELECT SQL_CALC_FOUND_ROWS * FROM processed_data WHERE mrt LIKE %s OR name LIKE %s LIMIT 12 OFFSET %s;", (keyword_format, keyword_format, offset_num,)) 
        attract_data = cursor.fetchall()
        cursor.execute("SELECT FOUND_ROWS();") 
        sum_rows = cursor.fetchone()[0] 
        next_page = page+1 if sum_rows > (page+1)*12 else None
        each_data_list = [{'id':each['id'],"name":each["name"],'category':each['category'], 'description':each['description'],'address':each['address'],'transport':each['transport'],'mrt':each['mrt'],'lat':each['lat'],'lng':each['lng'], 'images':json.loads(each['images'])} for each in attract_data]
        return JSONResponse(content={"data": each_data_list, "nextPage":next_page}, headers=headers)
        
    except mysql.connector.Error as err:
        return JSONResponse(    
            status_code=500,
            content={"error": True, "message": str(err)},
            headers=headers
        )
    finally:
        cursor.close()
        mydb.close()

@app.get("/api/attraction/{id}")  
def api_attractions(id=int): # page:int, keyword:str, 
    # print(id)
    try:
        mydb = mysql.connector.connect(**db_config, ssl_disabled=True)
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("SELECT * FROM processed_data WHERE id = %s", (id,)) 
        attract_data = cursor.fetchone()
        print(attract_data)

        if attract_data:
            each_data_list = [{'id':each['id'],"name":each["name"],'category':each['category'], 'description':each['description'],'address':each['address'],'transport':each['transport'],'mrt':each['mrt'],'lat':each['lat'],'lng':each['lng'], 'images':json.loads(each['images'])} for each in attract_data]
            return JSONResponse(content={"data": each_data_list},
                        headers=headers)
        else:
            return JSONResponse(    
                status_code=400,
                content={"error": True, "message": "inserted id out of range, valid id start from 1 to 58"},
                headers=headers
            )
    except mysql.connector.Error as err:
        return JSONResponse(    
            status_code=500,
            content={"error": True, "message": str(err)},
            headers=headers
        )
    finally:
        cursor.close()
        mydb.close()

# app.include_router(mrts.router)

@app.get("/api/mrts")
def api_mrts():
    mydb = None
    cursor = None
    try:
        # raise mysql.connector.Error("Manually triggered error for testing")
        mydb = mysql.connector.connect(**db_config, ssl_disabled=True)
        cursor = mydb.cursor()
        cursor.execute("SELECT mrt, COUNT(DISTINCT name) as count FROM processed_data WHERE mrt IS NOT NULL GROUP BY mrt ORDER BY count DESC;") 
        mrts_counted = cursor.fetchall()
        return JSONResponse(content={"data":[n[0] for n in mrts_counted]}, headers=headers)
    except mysql.connector.Error as err:
        return JSONResponse(    
            status_code=500,
            content={"error": True, "message": str(err)},
            headers=headers
        )
    finally:
        if cursor:
            cursor.close()
        if mydb:
            mydb.close()

# Static Pages (Never Modify Code in this Block)
@app.get("/", include_in_schema=False)
async def index(request: Request):
	return FileResponse("./static/index.html", media_type="text/html")
@app.get("/attraction/{id}", include_in_schema=False)
async def attraction(request: Request, id: int):
	return FileResponse("./static/attraction.html", media_type="text/html")
@app.get("/booking", include_in_schema=False)
async def booking(request: Request):
	return FileResponse("./static/booking.html", media_type="text/html")
@app.get("/thankyou", include_in_schema=False)
async def thankyou(request: Request):
	return FileResponse("./static/thankyou.html", media_type="text/html")