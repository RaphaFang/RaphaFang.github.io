from fastapi import FastAPI, Request, Form
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
        if request.url.path.startswith("/static/") or request.url.path.startswith("/square/"):
            return await call_next(request)

        if request.url.path == "/member":
            if not request.session.get('sign_in'): # 若user "sign_in" != True, 返回主頁面
                return RedirectResponse(url='/')
            
        if request.url.path not in ["/", "/signin", "/error","/square","/member","/signout"]:
            return RedirectResponse(url='/')
            # 換句話說，上方這串，意味著若是在 ["/", "/signin", "/error","/square","/member"] 這list中，便不需要檢查條件，直接進入該頁面
            # 解決下方"/signout" 一直被跳出的問題，原來是path auth 認證沒加上他，導致他的功能（清除cookie沒辦法運作），
        return await call_next(request)
         
    
user_info = {
    "test": "test"
}

app.mount("/static", StaticFiles(directory="static"), name="style")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse) 
async def display_html(request: Request):
    return templates.TemplateResponse(name = "api.html", request = request)

@app.get("/member", response_class=HTMLResponse)
async def show_successful_page(request: Request):
    return templates.TemplateResponse(name = "successful.html", context={"request" : request},request = request)

@app.get("/error", response_class=HTMLResponse)
async def show_error_page(request: Request,  message: str = "", title:str = "失敗頁面"):
    return templates.TemplateResponse(name = "error.html", context={"request": request, "message": message, "title":title},request = request)

@app.get("/square/{posit_num}" , response_class=HTMLResponse)
async def get_square(request: Request, posit_num:Optional[int]= None, message: str = "", title:str = "正整數平方計算結果"):
    message = posit_num**2
    return templates.TemplateResponse(name = "error.html", context={"request": request, "message": message, "title": title},request = request)

@app.post("/signin")
async def login(request: Request, username: Optional[str] = Form(None) , password:Optional[str] = Form(None), accept: bool = Form()):
    if username in user_info and password == user_info[username]:
        request.session['user'] = username
        request.session['sign_in'] = True
        print("Login successful, session:", dict(request.session))
        return RedirectResponse(url='/member', status_code=303)
    elif username is None or password is None:
        return RedirectResponse(url='/error?message=Please+enter+username+or+password', status_code=303)
    else:
        return RedirectResponse(url='/error?message=Username+or+password+is+not+correct', status_code=303)
 
@app.get("/signout")
async def signout(request: Request):
    # response.delete_cookie("session")
    request.session.clear() 
    # (X)並不是這裡沒清除，而是cookies ## 這裡確實沒有清除掉，「不是」因為html的<a>寫錯了
    # 嘗試print(dict)，發現兩個都沒有印出來，推測應該是整個@app.get("/signout")沒運作，導致cookie沒有清除
    ### 解決"/signout" 一直被跳出的問題，原來是path auth 認證沒加上他，導致他的功能（清除cookie沒辦法運作）
    ### cookie 沒有清除，導致我認為是上方/member的 auth條件沒寫好，怎麼每次登入完後在從url 打 /member都可以進入頁面

    return RedirectResponse(url='/', status_code=303)

app.add_middleware(AuthMiddleware)
app.add_middleware(SessionMiddleware, secret_key="whats_secret_key",max_age=3600)