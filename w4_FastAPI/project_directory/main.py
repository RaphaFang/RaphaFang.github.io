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


# mount css file
app.mount("/static_css", StaticFiles(directory="static_css"), name="static_css")
# https://fastapi.tiangolo.com/tutorial/static-files/
# Mount the static directory for CSS and JavaScript files

# mount css file

# https://fastapi.tiangolo.com/zh-hant/tutorial/request-forms-and-files/?h=form
@app.get("/login/")
async def login(username: str = Form(), password:str = Form(), accept: bool = Form()):
    # Your login logic here
    return {"username": username, "password": password, "accept": accept}

# uvicorn main:app --reload