from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

fashion = APIRouter()

templates = Jinja2Templates(directory="./templates")

@fashion.get('/fashion', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("fashion.html", { "request": request })
