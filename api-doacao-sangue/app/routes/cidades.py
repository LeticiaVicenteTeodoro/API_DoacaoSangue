from fastapi import APIRouter
from app.database import conectar

router = APIRouter(
    prefix="/cidades",
    tags=["Cidades"]
)


@router.get("/")
def listar_cidades():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    SELECT DISTINCT cidade, estado
    FROM hemocentros
    ORDER BY estado, cidade
    """)

    dados = cur.fetchall()
    conn.close()

    return [dict(item) for item in dados]


@router.get("/{estado}")
def listar_cidades_por_estado(estado: str):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    SELECT DISTINCT cidade, estado
    FROM hemocentros
    WHERE estado = ?
    ORDER BY cidade
    """, (estado.upper(),))

    dados = cur.fetchall()
    conn.close()

    return [dict(item) for item in dados]
