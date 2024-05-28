from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from typing import Optional
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import json

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

mydb = mysql.connector.connect(
  host="localhost",
  user=sql_username,
  password=sql_password,
  database="basic_db")

cursor = mydb.cursor()

# uvicorn main:app --reload
# cd /Users/fangsiyu/Desktop/wehelp/RaphaFang.github.io/part2/w1

app = FastAPI()

@app.get("/api/attractions")
def api_attractions(page=int,keyword=str):
    pass

@app.get("/api/attractions")  
def api_attractions(attractionId=int): # page:int, keyword:str, 
    cursor.execute("SELECT * FROM processed_data WHERE id = %s", (attractionId,)) 
    attract_data = cursor.fetchone()
    print(attract_data)

    if attract_data:
        return {"data":{'id':attract_data[0],"name":attract_data[1],'category':attract_data[2], 'description':attract_data[3],'address':attract_data[4],'transport':attract_data[5],'mrt':attract_data[6],'lat':attract_data[7],'lng':attract_data[8], 'images':json.loads(attract_data[9])}}
    else:
        return JSONResponse(    
            status_code=400,
            content={"error": True, "message": "景點編號不正確"}
        )
    
@app.get("/api/mrts")
def api_mrts():
    try:
        mydb = mysql.connector.connect(db_config)
        cursor = mydb.cursor()
        cursor.execute("SELECT mrt, COUNT(*) as count FROM processed_data GROUP BY mrt ORDER BY count DESC;") 
        mrts_counted = cursor.fetchall()
        return [n[0] for n in mrts_counted]
    
    except mysql.connector.Error as err:
        logger.error(f"Error: {err}")
        raise HTTPException(status_code=500, detail=f"Database error: {err}")

    finally:
        cursor.close()
        mydb.close()