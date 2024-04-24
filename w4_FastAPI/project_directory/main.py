from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

# uvicorn main:app --reload

app = FastAPI()

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/static/") or request.url.path.startswith("/square/"):
            response = await call_next(request)
            return response

        if request.url.path not in ["/", "/signin", "/error", "/member", "/square"]:
            if request.session.get('sign_in'):
                return RedirectResponse(url='/')
        
        response = await call_next(request)
        return response
    
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
        return RedirectResponse(url='/member', status_code=303)
    elif username is None or password is None:
        return RedirectResponse(url='/error?message=Please+enter+username+or+password', status_code=303)
    else:
        return RedirectResponse(url='/error?message=Username+or+password+is+not+correct', status_code=303)
    
@app.get("/signout")
async def signout(request: Request):
    request.session.pop('user', None)
    request.session.pop('sign_in', None)
    return RedirectResponse(url='/', status_code=303)

app.add_middleware(AuthMiddleware)
app.add_middleware(SessionMiddleware, secret_key="whats_secret_key")