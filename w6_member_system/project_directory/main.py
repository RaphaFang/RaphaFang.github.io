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
        if request.url.path not in ["/", "/signin", "/error","/square","/member","/signout", "/signup", '/createMessage',"/deleteMessage"]:
            return RedirectResponse(url='/')
        return await call_next(request)

app.mount("/static", StaticFiles(directory="static"), name="style")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse) 
async def display_html(request: Request):
    return templates.TemplateResponse(name = "api.html", request = request)

@app.get("/member", response_class=HTMLResponse)
async def show_successful_page(request: Request):
    username =request.session['name'] 
    print(username)
    user_id = request.session['member_id']
    print(user_id)

    cursor.execute("SELECT member.id, member.name,member.username,member.password,message.member_id, message.content, message.time AS message_time FROM member LEFT JOIN message message ON member.id = message.member_id ORDER BY message.time DESC LIMIT 5;") 
    messages_from_sql = cursor.fetchall()
    user_messages_list = [{"name": row[1], "content": row[5]} for row in messages_from_sql]

    return templates.TemplateResponse(name = "successful.html", context={"request": request, "username": username,'user_id':user_id, "user_messages_list":user_messages_list })

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
        request.session['name'] = existing_user[1]
        request.session['member_id'] = existing_user[0]
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
            cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)",(signup_username, signup_user_id, signup_password))
            mydb.commit() # 這步驟一定要作，不然資料寫不進去
            return RedirectResponse(url='/', status_code=303)
        
@app.post('/createMessage')
async def create_message(request: Request, input_message: Optional[str] = Form(None)):
    member_id = request.session['member_id']
    cursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)",(member_id,input_message))
    mydb.commit()
    return RedirectResponse(url='/member', status_code=303)
    
@app.post("/deleteMessage")
async def delete_message(request: Request, gonna_d_message_id: int = Form(...)):
    print(111)
    cursor.execute("DELETE FROM message WHERE id = %s", (gonna_d_message_id,))
    mydb.commit()
    return RedirectResponse(url="/member", status_code=303)

        
app.add_middleware(AuthMiddleware)
app.add_middleware(SessionMiddleware, secret_key="whats_secret_key",max_age=3600)