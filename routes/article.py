from fastapi import APIRouter

article = APIRouter()

@article.get('/articulo/{articulo_id}')
def index(article_id: str):
    test = article_id
    return {"articulo": f"Busqueda de {test}"}