from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

contact = APIRouter()

templates = Jinja2Templates(directory="./templates")

@contact.get('/contact', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("contact.html", { "request": request })
