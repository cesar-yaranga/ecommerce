from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

about = APIRouter()

templates = Jinja2Templates(directory="./templates")

@about.get('/about', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("about.html", { "request": request })
