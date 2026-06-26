from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Hemocentro
from app.schemas import (
    HemocentroCreate,
    HemocentroUpdate,
    HemocentroResponse,
)

router = APIRouter(
    prefix="/hemocentros",
    tags=["Hemocentros"]
)


@router.post("/", response_model=HemocentroResponse)
def criar_hemocentro(
    dados: HemocentroCreate,
    db: Session = Depends(get_db)
):
    novo = Hemocentro(**dados.model_dump())

    db.add(novo)
    db.commit()
    db.refresh(novo)

    return novo


@router.get("/", response_model=list[HemocentroResponse])
def listar_hemocentros(
    db: Session = Depends(get_db)
):
    return db.query(Hemocentro).all()


@router.get("/{hemocentro_id}", response_model=HemocentroResponse)
def buscar_hemocentro(
    hemocentro_id: int,
    db: Session = Depends(get_db)
):
    hemocentro = db.query(Hemocentro).filter(
        Hemocentro.id == hemocentro_id
    ).first()

    if not hemocentro:
        raise HTTPException(
            status_code=404,
            detail="Hemocentro não encontrado"
        )

    return hemocentro


@router.put("/{hemocentro_id}", response_model=HemocentroResponse)
def atualizar_hemocentro(
    hemocentro_id: int,
    dados: HemocentroUpdate,
    db: Session = Depends(get_db)
):
    hemocentro = db.query(Hemocentro).filter(
        Hemocentro.id == hemocentro_id
    ).first()

    if not hemocentro:
        raise HTTPException(
            status_code=404,
            detail="Hemocentro não encontrado"
        )

    for campo, valor in dados.model_dump().items():
        setattr(hemocentro, campo, valor)

    db.commit()
    db.refresh(hemocentro)

    return hemocentro


@router.delete("/{hemocentro_id}")
def deletar_hemocentro(
    hemocentro_id: int,
    db: Session = Depends(get_db)
):
    hemocentro = db.query(Hemocentro).filter(
        Hemocentro.id == hemocentro_id
    ).first()

    if not hemocentro:
        raise HTTPException(
            status_code=404,
            detail="Hemocentro não encontrado"
        )

    db.delete(hemocentro)
    db.commit()

    return {
        "mensagem": "Hemocentro deletado com sucesso"
    }


@router.get("/proximos/")
def listar_hemocentros_proximos():
    return {
        "mensagem": "Busca por proximidade será implementada depois"
    }