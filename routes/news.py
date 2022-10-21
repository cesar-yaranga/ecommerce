from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

news = APIRouter()

templates = Jinja2Templates(directory="./templates")

@news.get('/news', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("news.html", { "request": request })
