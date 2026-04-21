from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import Response
from pydantic import BaseModel
import time

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    # Executa a rota solicitada
    response = await call_next(request)

    process_time = time.time() - start_time
    print(f"{request.method} {request.url.path} - {process_time:.4f}s")

    return response


class User(BaseModel):
    name: str


class Item(BaseModel):
    name: str
    qty: int


@app.get("/api/v1/status")
async def api_status():
    return {"status": "ok", "api": "v1"}


@app.get("/api/v1/calc/sum")
async def calc_sum(a: int, b: int):
    return {"result": a + b}


@app.get("/api/v1/codes/{code}")
async def get_code(code: str):
    if code not in ("ok", "200"):
        raise HTTPException(status_code=404, detail="Código não encontrado")
    return {"code": code, "valid": True}


@app.head("/api/v1/ping")
async def ping_head():
    return Response(status_code=204)


@app.post("/api/v1/items")
async def create_item(item: Item):
    return {
        "received": item.name,
        "qty": item.qty,
        "note": f"Registrado: {item.qty} unidade(s) de {item.name}",
    }


@app.get("/")
async def hello_world():
    return {"message": "Hello, FastAPI!"}


@app.get("/api/v1/hello")
async def hello_name_via_query(name: str):
    return {"message": f"Hello {name}"}


@app.get("/api/v1/hello/{name}")
async def hello_name_via_path(name: str):
    return {"message": f"Hello {name}"}


@app.post("/api/v1/hello")
async def hello_name(user: User):
    return {"message": f"Hello {user.name}"}


@app.put("/api/v1/update")
async def user_update(user: User):
    return {"message": f"Recurso atualizado com o nome: {user.name}"}


@app.delete("/api/v1/delete")
async def delete_user_by_name(name: str):
    return {"message": f"Recurso deletado com o nome: {name}"}


@app.patch("/api/v1/patch")
async def patch_user(user: User):
    return {"message": f"Modificação parcial aplicada ao recurso com o nome: {user.name}"}