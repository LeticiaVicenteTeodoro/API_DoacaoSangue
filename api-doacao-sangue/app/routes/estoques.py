from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/estoques",
    tags=["Estoques"]
)


@router.get("/")
def listar_estoques(
    estado: str | None = Query(default=None),
    tipo_sanguineo: str | None = Query(default=None)
):
    conn = conectar()
    cur = conn.cursor()

    query = "SELECT * FROM estoques WHERE 1=1"
    params = []

    if estado:
        query += " AND estado = ?"
        params.append(estado.upper())

    if tipo_sanguineo:
        query += " AND tipo_sanguineo = ?"
        params.append(tipo_sanguineo.upper())

    cur.execute(query, params)
    dados = cur.fetchall()
    conn.close()

    return [dict(item) for item in dados]


@router.get("/criticos")
def listar_estoques_criticos():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    SELECT * FROM estoques
    WHERE lower(status) LIKE '%crítico%'
       OR lower(status) LIKE '%critico%'
       OR lower(status) LIKE '%alerta%'
    """)

    dados = cur.fetchall()
    conn.close()

    return [dict(item) for item in dados]
