from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from typing import Optional
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import json

from typing import Optional


import mysql.connector
import os
sql_password = os.getenv('SQL_PASSWORD')
sql_username = os.getenv('SQL_USER')
db_config = {
    'host': 'localhost',
    'user': sql_username,
    'password': sql_password,
    'database': 'basic_db',
}

# uvicorn main:app --reload
# cd /Users/fangsiyu/Desktop/wehelp/RaphaFang.github.io/part2/w1

app = FastAPI()
# http://127.0.0.1:8000/api/attractions?page=1
@app.get("/api/attractions")
def api_attractions(page: int=Query(..., ge=0), keyword: Optional[str] = None):
    # print(f"page = {page}, keyword = {keyword}")
    try:
        mydb = mysql.connector.connect(**db_config)
        cursor = mydb.cursor()
        offset_num = page*12
        keyword_format = f"%{keyword}%"  # 這邊不四多加上"""

        if keyword==None:
            cursor.execute("SELECT * FROM processed_data LIMIT 12 OFFSET %s;", (offset_num,)) 
            attract_data = cursor.fetchall()
            cursor.execute("SELECT COUNT(*) FROM processed_data;") 
            sum_rows = cursor.fetchone()[0]  # 不然出來的值會是turple, --> (58,)
            if sum_rows-(page+1)*12>0:
                next_page =  page+1
            else:
                next_page =  None
        else:
            cursor.execute("SELECT * FROM processed_data WHERE mrt LIKE %s OR name LIKE %s LIMIT 12 OFFSET %s;", (keyword_format, keyword_format, offset_num,)) 
            attract_data = cursor.fetchall()
            cursor.execute("SELECT COUNT(*) FROM processed_data  WHERE mrt LIKE %s OR name LIKE %s;", (keyword_format, keyword_format,)) 
            sum_rows = cursor.fetchone()[0] 
            if sum_rows-(page+1)*12>0:
                next_page =  page+1
            else:
                next_page =  None

        if attract_data:
            each_data_list = [{'id':each[0],"name":each[1],'category':each[2], 'description':each[3],'address':each[4],'transport':each[5],'mrt':each[6],'lat':each[7],'lng':each[8], 'images':json.loads(each[9])} for each in attract_data]
            return {"data": each_data_list, "nextPage":next_page}
        else:
            return {"data": [], "nextPage": None}    
        
    except mysql.connector.Error as err:
        return JSONResponse(    
            status_code=500,
            content={"error": True, "message": str(err)}
        )
    finally:
        cursor.close()
        mydb.close()

# http://127.0.0.1:8000/api/attraction?attractionId=1
@app.get("/api/attraction")  
def api_attractions(attractionId=int): # page:int, keyword:str, 
    print(attractionId)
    try:
        mydb = mysql.connector.connect(**db_config)
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM processed_data WHERE id = %s", (attractionId,)) 
        attract_data = cursor.fetchone()
        print(attract_data)

        if attract_data:
            return {"data":{'id':attract_data[0],"name":attract_data[1],'category':attract_data[2], 'description':attract_data[3],'address':attract_data[4],'transport':attract_data[5],'mrt':attract_data[6],'lat':attract_data[7],'lng':attract_data[8], 'images':json.loads(attract_data[9])}}
        else:
            return JSONResponse(    
                status_code=400,
                content={"error": True, "message": "inserted id out of range, valid id start from 1 to 58"}
            )
    except mysql.connector.Error as err:
        return JSONResponse(    
            status_code=500,
            content={"error": True, "message": str(err)}
        )
    finally:
        cursor.close()
        mydb.close()

# http://127.0.0.1:8000/api/mrts
@app.get("/api/mrts")
def api_mrts():
    try:
        # raise mysql.connector.Error("Manually triggered error for testing")
        mydb = mysql.connector.connect(**db_config)
        cursor = mydb.cursor()
        cursor.execute("SELECT mrt, COUNT(*) as count FROM processed_data GROUP BY mrt ORDER BY count DESC;") 
        mrts_counted = cursor.fetchall()
        return [n[0] for n in mrts_counted]
    except mysql.connector.Error as err:
        return JSONResponse(    
            status_code=500,
            content={"error": True, "message": str(err)}
        )
    finally:
        cursor.close()
        mydb.close()
