from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from fastapi import FastAPI, Request, HTTPException, Form
import re

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
# uvicorn main:app --reload
# cd /Users/fangsiyu/Desktop/wehelp/RaphaFang.github.io/w8/topic7


@app.get("/", response_class=HTMLResponse) 
async def display_html(request: Request):
    name = request.query_params.get("name")
    print(f"Received name parameter: {name}")  # Log the received parameter
    return templates.TemplateResponse(name = "api.html", request = request)

# http://127.0.0.1:8000
# http://127.0.0.1:8000?name=aaa
# http://127.0.0.1:8000?name=<img src="invalid_image" onerror="alert('XSS Attack!')">