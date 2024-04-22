from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount the static directory for CSS and JavaScript files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load templates from the templates directory
templates = Jinja2Templates(directory="templates")

# Define routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...), remember: bool = Form(...)):
    # Your login logic here
    return {"username": username, "password": password, "remember": remember}

# uvicorn main:app --reload