from fastapi import APIRouter, Query
from app.database import conectar

router = APIRouter(
    prefix="/hemocentros",
    tags=["Hemocentros"]
)


@router.get("/")
def listar_hemocentros(
    estado: str | None = Query(default=None),
    cidade: str | None = Query(default=None)
):
    conn = conectar()
    cur = conn.cursor()

    query = "SELECT * FROM hemocentros WHERE 1=1"
    params = []

    if estado:
        query += " AND estado = ?"
        params.append(estado.upper())

    if cidade:
        query += " AND cidade LIKE ?"
        params.append(f"%{cidade}%")

    cur.execute(query, params)
    dados = cur.fetchall()
    conn.close()

    return [dict(item) for item in dados]


@router.get("/proximos")
def listar_hemocentros_proximos(
    cidade: str = Query(..., description="Cidade de referência")
):
    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM hemocentros WHERE cidade LIKE ?",
        (f"%{cidade}%",)
    )

    dados = cur.fetchall()
    conn.close()

    return {
        "cidade_referencia": cidade,
        "resultados": [dict(item) for item in dados]
    }
