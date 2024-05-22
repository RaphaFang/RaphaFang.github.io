from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# uvicorn main:app --reload
# cd /Users/fangsiyu/Desktop/wehelp/RaphaFang.github.io/w8/topic4_project_directory

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse) 
async def display_html(request: Request):
    return templates.TemplateResponse(name = "api.html", request = request)


@app.get("/api/data")
async def get_data():
    return {"message": "This is a CORS-enabled response"}

@app.post("/api/simple")
async def post_simple(data: dict):
    return {"message": "Simple request received", "data": data}

@app.post("/api/preflight")
async def post_preflight(data: dict):
    return {"message": "Preflight request received", "data": data}