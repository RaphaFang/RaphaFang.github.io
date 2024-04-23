from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

# import html file
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse) # By declaring response_class=HTMLResponse the docs UI will be able to know that the response will be HTML.
async def display_html(request: Request):
    return templates.TemplateResponse(name = "api.html", request = request)
# https://fastapi.tiangolo.com/advanced/templates/


# mount static for CSS and js
app.mount("/static", StaticFiles(directory="static"), name="static_css")
# app.mount("/static_js", StaticFiles(directory="static"), name="static_js")
# 第一个 "/static" 是 URL 路径前缀。directory="static" 是服务器上的文件夹路径。name="static" 是这个挂载点的内部名称，用于应用程序内部引用。
# https://fastapi.tiangolo.com/tutorial/static-files/


# https://fastapi.tiangolo.com/zh-hant/tutorial/request-forms-and-files/?h=form
@app.post("/signin")
async def login(username: str = Form(), password:str = Form(), accept: bool = Form()):
    # Your login logic here
    return {"username": username, "password": password, "accept": accept}

# uvicorn main:app --reload


# -------------------------------------------------------------------------------------------
# 明天的代作事項
# js要處理好阻擋送資料，如果未打溝

# O 解決：py 要處理應該是收到數據資料，而不是 detal : no found
#       改成 post 解可以收到資訊