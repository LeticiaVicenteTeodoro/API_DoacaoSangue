from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Estoque, Hemocentro
from app.schemas import (
    EstoqueCreate,
    EstoqueUpdate,
    EstoqueResponse,
)

router = APIRouter(
    prefix="/estoques",
    tags=["Estoques"]
)


@router.post("/", response_model=EstoqueResponse)
def criar_estoque(
    dados: EstoqueCreate,
    db: Session = Depends(get_db)
):
    hemocentro = db.query(Hemocentro).filter(
        Hemocentro.id == dados.hemocentro_id
    ).first()

    if not hemocentro:
        raise HTTPException(
            status_code=404,
            detail="Hemocentro não encontrado"
        )

    novo = Estoque(**dados.model_dump())

    db.add(novo)
    db.commit()
    db.refresh(novo)

    return novo


@router.get("/", response_model=list[EstoqueResponse])
def listar_estoques(
    estado: str | None = None,
    tipo_sanguineo: str | None = None,
    db: Session = Depends(get_db)
):
    consulta = db.query(Estoque)

    if tipo_sanguineo:
        consulta = consulta.filter(
            Estoque.tipo_sanguineo == tipo_sanguineo
        )

    if estado:
        consulta = consulta.join(Hemocentro).filter(
            Hemocentro.estado == estado
        )

    return consulta.all()


@router.get("/criticos", response_model=list[EstoqueResponse])
def listar_estoques_criticos(
    db: Session = Depends(get_db)
):
    return db.query(Estoque).filter(
        Estoque.status.in_(["Crítico", "Critico", "Alerta"])
    ).all()


@router.get("/{estoque_id}", response_model=EstoqueResponse)
def buscar_estoque(
    estoque_id: int,
    db: Session = Depends(get_db)
):
    estoque = db.query(Estoque).filter(
        Estoque.id == estoque_id
    ).first()

    if not estoque:
        raise HTTPException(
            status_code=404,
            detail="Estoque não encontrado"
        )

    return estoque


@router.put("/{estoque_id}", response_model=EstoqueResponse)
def atualizar_estoque(
    estoque_id: int,
    dados: EstoqueUpdate,
    db: Session = Depends(get_db)
):
    estoque = db.query(Estoque).filter(
        Estoque.id == estoque_id
    ).first()

    if not estoque:
        raise HTTPException(
            status_code=404,
            detail="Estoque não encontrado"
        )

    for campo, valor in dados.model_dump().items():
        setattr(estoque, campo, valor)

    db.commit()
    db.refresh(estoque)

    return estoque


@router.delete("/{estoque_id}")
def deletar_estoque(
    estoque_id: int,
    db: Session = Depends(get_db)
):
    estoque = db.query(Estoque).filter(
        Estoque.id == estoque_id
    ).first()

    if not estoque:
        raise HTTPException(
            status_code=404,
            detail="Estoque não encontrado"
        )

    db.delete(estoque)
    db.commit()

    return {
        "mensagem": "Estoque deletado com sucesso"
    }