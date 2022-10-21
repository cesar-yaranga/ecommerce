from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Rutas
from routes.home import home
from routes.about import about
from routes.contact import contact
from routes.fashion import fashion
from routes.news import news
from routes.products import products
from routes.article import article
from routes.search import search
from routes.post import post

app = FastAPI()

app.mount("/static/", StaticFiles(directory="static"), name="static")

app.include_router(home)
app.include_router(about)
app.include_router(products)
app.include_router(fashion)
app.include_router(news)
app.include_router(contact)

# Others
app.include_router(article)
app.include_router(search)
# app.include_router(post)