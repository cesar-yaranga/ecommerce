from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

home = APIRouter()

templates = Jinja2Templates(directory="./templates")

@home.get('/', response_class=HTMLResponse)
@home.get('/index', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", { "request": request })
