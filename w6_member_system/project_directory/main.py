import mysql.connector
import os
sql_password = os.getenv('SQL_PASSWORD')
sql_username = os.getenv('SQL_USER')

mydb = mysql.connector.connect(
  host="localhost",
  user=sql_username,
  password=sql_password,
  database="website")

cursor = mydb.cursor()

from fastapi import FastAPI, Request, Form, Cookie, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

# uvicorn main:app --reload
# max_age=3600 一小時的登入cookies

app = FastAPI()
class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/static/"):
            return await call_next(request)
        if request.url.path == "/member":
            if not request.session.get('sign_in'): 
                return RedirectResponse(url='/')
        if request.url.path == "/createMessage":
            if not request.session.get('sign_in'): 
                return RedirectResponse(url='/')
        if request.url.path not in ["/", "/signin", "/error","/square","/member","/signout", "/signup", '/createMessage']:
            return RedirectResponse(url='/')
        return await call_next(request)
    

app.mount("/static", StaticFiles(directory="static"), name="style")
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse) 
async def display_html(request: Request):
    return templates.TemplateResponse(name = "api.html", request = request)

@app.get("/member", response_class=HTMLResponse)
async def show_successful_page(request: Request):
    message =request.session['message'] 
    print(message)
    return templates.TemplateResponse(name = "successful.html", context={"request": request, "message": message})

@app.get("/error", response_class=HTMLResponse)
async def show_error_page(request: Request,  message: str = "", title:str = "失敗頁面"): #帳號或密碼輸入錯誤
    return templates.TemplateResponse(name = "error.html", context={"request": request, "message": message, "title":title},request = request)

@app.post("/signin")
async def login(request: Request, response: Response,username:Optional[str] = Form(None) , password:Optional[str] = Form(None)):
    cursor.execute("SELECT * FROM member WHERE username = %s", (username,)) # signup_username, ，這個逗號一定要加上
    existing_user = cursor.fetchone() # 這一步驟，做到檢索、讀取檢索答案的第一行      
    if existing_user == None:
        return RedirectResponse(url='/error?message=Username+or+password+is+not+correct', status_code=303)
    correct_password = existing_user[3]
    if correct_password == password:
        request.session['user'] = username
        request.session['sign_in'] = True
        request.session['message'] = existing_user[1]
        # return response
        return RedirectResponse(url="/member", status_code=303 )
    else:
        return RedirectResponse(url='/error?message=Username+or+password+is+not+correct', status_code=303)
 
@app.get("/signout")
async def signout(request: Request):
    request.session.clear() 
    return RedirectResponse(url='/', status_code=303)

@app.post("/signup")
async def login(request: Request, signup_username: Optional[str] = Form(None) ,signup_user_id : Optional[str] = Form(None) ,signup_password:Optional[str] = Form(None)):
    if signup_user_id:
        cursor.execute("SELECT * FROM member WHERE username = %s", (signup_user_id,)) # signup_username, ，這個逗號一定要加上
        existing_user = cursor.fetchone() # 這一步驟，做到檢索、讀取檢索答案的第一行        
        if existing_user:
            return RedirectResponse(url='/error?message=Repeated+username', status_code=303)
        else:
            build_user_sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
            cursor.execute(build_user_sql,(signup_username, signup_user_id, signup_password))
            mydb.commit() # 這步驟一定要作，不然資料寫不進去
            return RedirectResponse(url='/', status_code=303)
        
# @app.post('/createMessage')
# async def create_message(request: Request, input_message: Optional[str] = Form(None)):
#     # if request.session['sign_in'] = True:


app.add_middleware(AuthMiddleware)
app.add_middleware(SessionMiddleware, secret_key="whats_secret_key",max_age=3600)