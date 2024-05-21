from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse


from pydantic import BaseModel, Field, validator
import re

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# uvicorn main:app --reload
# cd /Users/fangsiyu/Desktop/wehelp/RaphaFang.github.io/w8/topic3_project_directory


class DataModel(BaseModel):
    email: str
    password: str = Field(..., min_length=4, max_length=8)
    tel:str

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
    
@app.get("/", response_class=HTMLResponse) 
async def display_html(request: Request):
    return templates.TemplateResponse(name = "api.html", request = request)


@app.post("/verify")
async def verify_data(data: DataModel):

    return {"message": "Data is valid"}