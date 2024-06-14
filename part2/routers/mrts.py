from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/api/mrts")
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