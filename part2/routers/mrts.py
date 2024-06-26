from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import mysql.connector

router = APIRouter()
headers = {"Content-Type": "application/json; charset=utf-8"}

@router.get("/api/mrts")
async def api_mrts(request: Request):
    mydb = None
    cursor = None
    try:
        db_pool = request.state.db_pool.get("basic_db") # 要透過get()，不然db_pool得到的都會是字典不會是真正的連接，但是這有點太奇怪，叫出來的東西理論上都一樣啊
        print(type(request.state.db_pool))
        print(request.state.db_pool)
        connection = db_pool.get_connection()
        cursor = connection.cursor()

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
        if connection:
            connection.close()

