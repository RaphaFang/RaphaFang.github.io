from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware

import requests



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# uvicorn main:app --reload
# cd /Users/fangsiyu/Desktop/wehelp/RaphaFang.github.io/w8/topic4_project_directory

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows requests from specified origins
    allow_credentials=True,  # Allows cookies to be included in requests
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/", response_class=HTMLResponse) 
async def display_html(request: Request):
    return templates.TemplateResponse(name = "api.html", request = request)

@app.get("/proxy/google")
async def proxy_google():
    response = requests.get("https://www.google.com")
    return response.text

@app.get("/api/data")
async def get_data():
    return {"message": "This is a CORS-enabled response"}

@app.post("/api/simple")
async def post_simple(data: dict):
    return {"message": "Simple request received", "data": data}

@app.post("/api/preflight")
async def post_preflight(data: dict):
    return {"message": "Preflight request received", "data": data}



# response = requests.get("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json")
# print(response.json())