from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Hemocentro

router = APIRouter(
    prefix="/cidades",
    tags=["Cidades"]
)


@router.get("/")
def listar_cidades(db: Session = Depends(get_db)):
    cidades = db.query(
        Hemocentro.estado,
        Hemocentro.cidade
    ).distinct().all()

    return [
        {
            "estado": estado,
            "cidade": cidade
        }
        for estado, cidade in cidades
    ]


@router.get("/{estado}")
def listar_cidades_por_estado(
    estado: str,
    db: Session = Depends(get_db)
):
    cidades = db.query(Hemocentro.cidade).filter(
        Hemocentro.estado == estado.upper()
    ).distinct().all()

    return [
        cidade[0]
        for cidade in cidades
    ]