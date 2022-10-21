from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

products = APIRouter()

templates = Jinja2Templates(directory="./templates")

@products.get('/products', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("products.html", { "request": request })
