from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from fastapi import FastAPI, Request, HTTPException, Form
from pydantic import BaseModel, Field, validator
import re

app = FastAPI()
templates = Jinja2Templates(directory="templates")
# uvicorn main:app --reload
# cd /Users/fangsiyu/Desktop/wehelp/RaphaFang.github.io/w8/topic3_project_directory

class DataModel(BaseModel):
    email: str
    password: str
    tel: str
 
    @validator('email')
    def validate_email(cls, v):
        if not re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", v):
            raise ValueError('Invalid email format')
        return v

    @validator('password')
    def validate_password(cls, v):
        if not re.match(r"^[A-Za-z0-9@#$%]{4,8}$", v):
            raise ValueError('Password must be 4-8 characters long and include only alphabets, numbers, and @#$%')
        return v
    
    @validator('tel')
    def validate_tel(cls, v):
        if not re.match(r"^[0-9]{4}-[0-9]{3}-[0-9]{3}$", v):
            raise ValueError('tel problem')
        return v

@app.post("/verify")
async def verify_data(email: str = Form(...), password: str = Form(...), tel: str= Form(...)): 
    # 上方的password: str = Form(...)，抓的資料是html的name="tel"，所以html 沒東西時，就會報錯，顯示資訊空缺
    try:
        data = DataModel(email=email, password=password, tel=tel)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": "Data is valid"}

@app.get("/", response_class=HTMLResponse) 
async def display_html(request: Request):
    return templates.TemplateResponse(name = "api.html", request = request)