from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Annotated , Optional

from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

app = FastAPI()
# from your_application.middleware import AuthMiddleware
# app.add_middleware(AuthMiddleware)

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 新增一個允許static資料夾東西可以讀取的通道
        if request.url.path.startswith("/static/"):
            response = await call_next(request)
            return response
        # 阻擋未從指定端口進來
        if request.url.path not in ["/", "/signin", "/error", "/member"]:
            # 阻擋如果['sign_in']是True
            if 'sign_in' in request.session:
                # not request.session['sign_in']，這會得到 KeyError: 'sign_in'
                # 若為True，則回到主頁面
                return RedirectResponse(url='/')
        response = await call_next(request)
        return response
    
# mount static for CSS and js
app.mount("/static", StaticFiles(directory="static"), name="style")
# app.mount("/static", StaticFiles(directory="static"), name="successful")
# app.mount("/static_js", StaticFiles(directory="static"), name="static_js")
# 第一个 "/static" 是 URL 路径前缀。directory="static" 是服务器上的文件夹路径。name="static" 是这个挂载点的内部名称，用于应用程序内部引用。
# https://fastapi.tiangolo.com/tutorial/static-files/

# def html_generator(text):
    # html_content = f"""
    # <!DOCTYPE html>
    # <html lang="en">
    #   <head>
    #     <meta charset="UTF-8" />
    #     <title>login page</title>
    #     <link rel="stylesheet" href="static/successful.css">
    #     <!-- <script src="/static/script.js"></script> -->
    #   </head>
    #   <body>
    #     <div class="container">
    #     <div class="login-header">
    #         <p>失敗頁面</p>
    #     </div>
    #     <p class = "text">{text}</p></br></p>
    #     </div>
    #   </body>
    # </html>
    # """
    # return HTMLResponse(content=html_content, status_code=200)

# user information data
user_info = {
    "test": "test"
}

# import html file
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse) # By declaring response_class=HTMLResponse the docs UI will be able to know that the response will be HTML.
async def display_html(request: Request):
    return templates.TemplateResponse(name = "api.html", request = request)
# https://fastapi.tiangolo.com/advanced/templates/

@app.get("/member", response_class=HTMLResponse)
async def show_successful_page(request: Request):
    return templates.TemplateResponse(name = "successful.html", context={"request" : request},request = request)
    # return templates.TemplateResponse(name = "successful.html", request = request)

@app.get("/error", response_class=HTMLResponse)
async def show_error_page(request: Request,  message: str = ""):
    return templates.TemplateResponse(name = "error.html", context={"request": request, "message": message},request = request)
# https://fastapi.tiangolo.com/zh-hant/tutorial/request-forms-and-files/?h=form

@app.post("/signin")
async def login(request: Request, username: Optional[str] = Form(None) , password:Optional[str] = Form(None), accept: bool = Form()):
    # user_input =  {"username": username, "password": password, "accept": accept}

    if username in user_info and password == user_info[username]:
        request.session['user'] = username
        request.session['sign_in'] = True
        return RedirectResponse(url='/member', status_code=303)
        # status_code=303, the server tells the client to redirect to /member but to use the GET method instead of POST.
    elif username is None or password is None:
        return RedirectResponse(url='/error?message=Please+enter+username+or+password', status_code=303)
        # return html_generator("Please enter username or password")
    else:
        return RedirectResponse(url='/error?message=Username+or+password+is+not+correct', status_code=303)
        # return html_generator("Username or password is not correct")
    
@app.get("/signout")
async def signout(request: Request):
    # 寫一個登入條件為 false的request調整
    request.session.pop('user', None)
    request.session.pop('sign_in', None)
    return RedirectResponse(url='/', status_code=303)


app.add_middleware(AuthMiddleware)
app.add_middleware(SessionMiddleware, secret_key="whats_secret_key")
# 這要在最後一行，才不會報錯 ：AssertionError: SessionMiddleware must be installed to access request.session




# uvicorn main:app --reload



# -------------------------------------------------------------------------------------------
# 明天的代作事項
# O 解決：js要處理好阻擋送資料，如果未打溝
# O 解決：py 要處理應該是收到數據資料，而不是 detal : no found
#       改成 post 解可以收到資訊
# -------------------------------------------------------------------------------------------
# O 解決：處理css檔案被讀錯，這到底是怎麼發生的？？？？？？
# 又又又又又又又又又又又又又又又又又又發生css連結斷掉的問題... 近乎崩潰...