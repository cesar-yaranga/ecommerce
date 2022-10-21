from fastapi import APIRouter

search = APIRouter()

@search.get('/search/{cotegories}')
def index(categorias: str):
    test = cotegories
    return {"buscar": f"Busqueda de {test}"}