from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse

from typing import Annotated
from flask import request

app = FastAPI()


# import html file
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse) # By declaring response_class=HTMLResponse the docs UI will be able to know that the response will be HTML.
async def display_html(request: Request):
    return templates.TemplateResponse(name = "api.html", request = request)
# https://fastapi.tiangolo.com/advanced/templates/

# @app.get("/member", response_class=HTMLResponse)
# async def redirect_successful_html():
#     return templates.TemplateResponse(name = "successful.html", request = request)


# mount static for CSS and js
app.mount("/static", StaticFiles(directory="static"), name="static_css")
# app.mount("/static_js", StaticFiles(directory="static"), name="static_js")
# 第一个 "/static" 是 URL 路径前缀。directory="static" 是服务器上的文件夹路径。name="static" 是这个挂载点的内部名称，用于应用程序内部引用。
# https://fastapi.tiangolo.com/tutorial/static-files/


# https://fastapi.tiangolo.com/zh-hant/tutorial/request-forms-and-files/?h=form
@app.post("/signin")
async def login(username: Annotated[str, Form()] , password:Annotated[str, Form()], accept: Annotated[bool, Form()]):
    user_info =  {"username": username, "password": password, "accept": accept}
    if user_info["username"] == "test" and user_info["password"] == "test":
        print("you are at 31")
        # return RedirectResponse('http://127.0.0.1:8000/member')


                    # return {"message": "登入成功"}
# successful
# @app.get("/member")

# @app.get("/error?message=自訂的錯誤訊息")


# uvicorn main:app --reload


# -------------------------------------------------------------------------------------------
# 明天的代作事項
# js要處理好阻擋送資料，如果未打溝

# O 解決：py 要處理應該是收到數據資料，而不是 detal : no found
#       改成 post 解可以收到資訊