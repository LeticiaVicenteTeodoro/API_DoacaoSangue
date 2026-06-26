from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Campanha
from app.schemas import (
    CampanhaCreate,
    CampanhaUpdate,
    CampanhaResponse
)

router = APIRouter(
    prefix="/campanhas",
    tags=["Campanhas"]
)


@router.post("/", response_model=CampanhaResponse)
def criar_campanha(
    dados: CampanhaCreate,
    db: Session = Depends(get_db)
):
    campanha = Campanha(**dados.model_dump())

    db.add(campanha)
    db.commit()
    db.refresh(campanha)

    return campanha


@router.get("/", response_model=list[CampanhaResponse])
def listar_campanhas(
    estado: str | None = None,
    cidade: str | None = None,
    db: Session = Depends(get_db)
):
    consulta = db.query(Campanha)

    if estado:
        consulta = consulta.filter(Campanha.estado == estado)

    if cidade:
        consulta = consulta.filter(Campanha.cidade == cidade)

    return consulta.all()


@router.get("/ativas", response_model=list[CampanhaResponse])
def campanhas_ativas(
    db: Session = Depends(get_db)
):
    return db.query(Campanha).filter(
        Campanha.ativa == True
    ).all()


@router.get("/{campanha_id}", response_model=CampanhaResponse)
def buscar_campanha(
    campanha_id: int,
    db: Session = Depends(get_db)
):
    campanha = db.query(Campanha).filter(
        Campanha.id == campanha_id
    ).first()

    if not campanha:
        raise HTTPException(404, "Campanha não encontrada")

    return campanha


@router.put("/{campanha_id}", response_model=CampanhaResponse)
def atualizar_campanha(
    campanha_id: int,
    dados: CampanhaUpdate,
    db: Session = Depends(get_db)
):
    campanha = db.query(Campanha).filter(
        Campanha.id == campanha_id
    ).first()

    if not campanha:
        raise HTTPException(404, "Campanha não encontrada")

    for campo, valor in dados.model_dump().items():
        setattr(campanha, campo, valor)

    db.commit()
    db.refresh(campanha)

    return campanha


@router.delete("/{campanha_id}")
def deletar_campanha(
    campanha_id: int,
    db: Session = Depends(get_db)
):
    campanha = db.query(Campanha).filter(
        Campanha.id == campanha_id
    ).first()

    if not campanha:
        raise HTTPException(404, "Campanha não encontrada")

    db.delete(campanha)
    db.commit()

    return {
        "mensagem": "Campanha removida com sucesso"
    }