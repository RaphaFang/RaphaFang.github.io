from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Annotated , Optional

app = FastAPI()

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

# import html file
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse) # By declaring response_class=HTMLResponse the docs UI will be able to know that the response will be HTML.
async def display_html(request: Request):
    return templates.TemplateResponse(name = "api.html", request = request)
# https://fastapi.tiangolo.com/advanced/templates/

@app.get("/member", response_class=HTMLResponse)
async def redirect_successful_html(request: Request):
    return templates.TemplateResponse(name = "successful.html", context={"request" : request},request = request)
    # return templates.TemplateResponse(name = "successful.html", request = request)


@app.get("/error", response_class=HTMLResponse)
async def show_error_page(request: Request,  message: str = ""):
    return templates.TemplateResponse(name = "error.html", context={"request": request, "message": message},request = request)

# https://fastapi.tiangolo.com/zh-hant/tutorial/request-forms-and-files/?h=form
@app.post("/signin")
async def login(username: Optional[str] = Form(None) , password:Optional[str] = Form(None), accept: bool = Form()):
    user_info =  {"username": username, "password": password, "accept": accept}
    if user_info["username"] == "test" and user_info["password"] == "test":
        return RedirectResponse(url='/member', status_code=303)
        # status_code=303, the server tells the client to redirect to /member but to use the GET method instead of POST.
    elif user_info["username"] is None or user_info["password"] is None:
        return RedirectResponse(url='/error?message=Please+enter+username+or+password', status_code=303)
        # return html_generator("Please enter username or password")
    else:
        return RedirectResponse(url='/error?message=Username+or+password+is+not+correct', status_code=303)
        # return html_generator("Username or password is not correct")





# uvicorn main:app --reload



# -------------------------------------------------------------------------------------------
# 明天的代作事項
# O 解決：js要處理好阻擋送資料，如果未打溝
# O 解決：py 要處理應該是收到數據資料，而不是 detal : no found
#       改成 post 解可以收到資訊
# -------------------------------------------------------------------------------------------
# O 解決：處理css檔案被讀錯，這到底是怎麼發生的？？？？？？