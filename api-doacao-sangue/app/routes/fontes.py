from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import FonteDados
from app.schemas import (
    FonteDadosCreate,
    FonteDadosUpdate,
    FonteDadosResponse
)

router = APIRouter(
    prefix="/fontes",
    tags=["Fontes de Dados"]
)


@router.post("/", response_model=FonteDadosResponse)
def criar_fonte(
    dados: FonteDadosCreate,
    db: Session = Depends(get_db)
):
    fonte = FonteDados(**dados.model_dump())

    db.add(fonte)
    db.commit()
    db.refresh(fonte)

    return fonte


@router.get("/", response_model=list[FonteDadosResponse])
def listar_fontes(
    estado: str | None = None,
    db: Session = Depends(get_db)
):
    consulta = db.query(FonteDados)

    if estado:
        consulta = consulta.filter(
            FonteDados.estado == estado.upper()
        )

    return consulta.all()


@router.get("/{fonte_id}", response_model=FonteDadosResponse)
def buscar_fonte(
    fonte_id: int,
    db: Session = Depends(get_db)
):
    fonte = db.query(FonteDados).filter(
        FonteDados.id == fonte_id
    ).first()

    if not fonte:
        raise HTTPException(404, "Fonte não encontrada")

    return fonte


@router.put("/{fonte_id}", response_model=FonteDadosResponse)
def atualizar_fonte(
    fonte_id: int,
    dados: FonteDadosUpdate,
    db: Session = Depends(get_db)
):
    fonte = db.query(FonteDados).filter(
        FonteDados.id == fonte_id
    ).first()

    if not fonte:
        raise HTTPException(404, "Fonte não encontrada")

    for campo, valor in dados.model_dump().items():
        setattr(fonte, campo, valor)

    db.commit()
    db.refresh(fonte)

    return fonte


@router.delete("/{fonte_id}")
def deletar_fonte(
    fonte_id: int,
    db: Session = Depends(get_db)
):
    fonte = db.query(FonteDados).filter(
        FonteDados.id == fonte_id
    ).first()

    if not fonte:
        raise HTTPException(404, "Fonte não encontrada")

    db.delete(fonte)
    db.commit()

    return {
        "mensagem": "Fonte removida com sucesso"
    }