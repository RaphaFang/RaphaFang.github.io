from fastapi import FastAPI, Request, Form, Cookie, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
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
        if request.url.path == "/createMessage" or request.url.path == "/deleteMessage":
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
    user_id = request.session['member_id']

    cursor.execute("SELECT member.id, member.name,member.username,member.password,message.id AS message_id,message.member_id, message.content, message.time AS message_time FROM member LEFT JOIN message message ON member.id = message.member_id ORDER BY message.time DESC LIMIT 5;") 
    messages_from_sql = cursor.fetchall()
    user_messages_list = [{"name": row[1], 'message_id': row[4],'member_id':row[5], "content": row[6], "hidden_state":user_id==row[5]} for row in messages_from_sql]
        #! 讀取JOIN 後的 member.name / member.username / member.password 以及 message.id AS message_id / message.member_id / message.content /  message.time AS message_time 
    return templates.TemplateResponse(name = "successful.html", context={"request": request, "username": username,'user_id':user_id, "user_messages_list":user_messages_list })

@app.get("/error", response_class=HTMLResponse)
async def show_error_page(request: Request,  message: str = "", title:str = "失敗頁面"): #帳號或密碼輸入錯誤
    return templates.TemplateResponse(name = "error.html", context={"request": request, "message": message, "title":title},request = request)

@app.post("/signin")
async def login(request: Request, response: Response, username:Optional[str] = Form(None) , password:Optional[str] = Form(None)):
    cursor.execute("SELECT * FROM member WHERE username = %s", (username,)) # username, ，這個逗號一定要加上
    apply_sign_user = cursor.fetchone() # 這一步驟，做到檢索、讀取檢索答案的第一行      
    if apply_sign_user == None:
        return RedirectResponse(url='/error?message=Username+or+password+is+not+correct', status_code=303)
    
    correct_password = apply_sign_user[3]
    if password == correct_password:
        request.session['user'] = username
        request.session['sign_in'] = True
        request.session['name'] = apply_sign_user[1]
        request.session['member_id'] = apply_sign_user[0]
        return RedirectResponse(url="/member", status_code=303 )
    else:
        return RedirectResponse(url='/error?message=Username+or+password+is+not+correct', status_code=303)
 
@app.get("/signout")
async def signout(request: Request):
    request.session.clear() 
    return RedirectResponse(url='/', status_code=303)

@app.post("/signup")
async def login(request: Request, signup_username: Optional[str] = Form(None) ,signup_user_id : Optional[str] = Form(None) ,signup_password:Optional[str] = Form(None)):
    if signup_user_id: # ! 確保不是空字串
        cursor.execute("SELECT * FROM member WHERE username = %s", (signup_user_id,)) # signup_username, ，這個逗號一定要加上
        existing_user_checking = cursor.fetchone() # 這一步驟，做到檢索、讀取檢索答案的第一行        
        if existing_user_checking:
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
async def delete_message(request: Request, data_from_html: str = Form(...)):
    print('/deleteMessage functioning...')

    html_message_id, html_member_id  = data_from_html.split("|")
    print(f"the id of msg: {html_message_id},the id of msg creator: {html_member_id}")

    if request.session['member_id'] == int(html_member_id) and request.session['sign_in']==True:  # 從html讀過來，因為我輸入多比資料，透過str，要轉成int
        cursor.execute("DELETE FROM message WHERE id = %s AND member_id = %s", (html_message_id,html_member_id))
        mydb.commit()
        print('mydb.commit()--- check database delete or not?')
    return RedirectResponse(url="/member", status_code=303)

app.add_middleware(AuthMiddleware)
app.add_middleware(SessionMiddleware, secret_key="whats_secret_key",max_age=3600)


# O解決：現在可以正常刪除留言
# O解決：處理按鈕隱藏問題
# O解決：處理刪除實驗政用戶與留言建立者id
# O解決：將檔案名重新處理