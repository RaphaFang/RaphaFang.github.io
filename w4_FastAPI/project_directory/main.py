from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

# uvicorn main:app --reload
# max_age=5 僅有5秒的登入cookies

app = FastAPI()

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/static/") or request.url.path.startswith("/square/"):
            return await call_next(request)

        if request.url.path == "/member":
            if not request.session.get('sign_in'): # 若user "sign_in" != True, 返回主頁面
                return RedirectResponse(url='/')
            
        if request.url.path not in ["/", "/signin", "/error","/square","/member"]:
            return RedirectResponse(url='/')
            # 換句話說，上方這串，意味著若是在 ["/", "/signin", "/error","/square","/member"] 這list中，便不需要檢查條件，直接進入該頁面
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
    # request.session.pop('user', None)
    # request.session.pop('sign_in', None)
    request.session.clear() #並不是這裡沒清除，而是cookies
    return RedirectResponse(url='/', status_code=303)

app.add_middleware(AuthMiddleware)
app.add_middleware(SessionMiddleware, secret_key="whats_secret_key",max_age=5)


# max_age=5
# 沒有設置這個，導致if request.url.path == "/member": 條件一直無法觸發
# 以及導致，我試圖移除list的member，導致form登入也進不去，if request.url.path not in ["/", "/signin", "/error","/square","/member"]:
        # if request.url.path == "/member":
        #     if not request.session.get('sign_in'): # 若user "sign_in" != True, 返回主頁面
        #         return RedirectResponse(url='/')
            
        # if request.url.path not in ["/", "/signin", "/error","/square","/member"]:
        #     return RedirectResponse(url='/')
        #     # 換句話說，上方這串，意味著若是在 ["/", "/signin", "/error","/square"] 這list中，便不需要檢查條件，直接進入該頁面
        # return await call_next(request)