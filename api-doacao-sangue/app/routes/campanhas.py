from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/campanhas",
    tags=["Campanhas"]
)


@router.get("/")
def listar_campanhas(
    estado: str | None = Query(default=None),
    cidade: str | None = Query(default=None)
):
    conn = conectar()
    cur = conn.cursor()

    query = "SELECT * FROM campanhas WHERE 1=1"
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


@router.get("/ativas")
def listar_campanhas_ativas():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("SELECT * FROM campanhas")
    dados = cur.fetchall()
    conn.close()

    return [dict(item) for item in dados]
