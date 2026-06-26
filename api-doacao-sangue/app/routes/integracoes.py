from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import get_db
from app.models import Hemocentro, Estoque
from app.services.hemominas import coletar_estoque_hemominas

router = APIRouter(
    prefix="/integracoes",
    tags=["Integrações"]
)


@router.post("/hemominas/estoques")
def atualizar_estoque_hemominas(
    db: Session = Depends(get_db)
):
    dados = coletar_estoque_hemominas()

    if not dados:
        raise HTTPException(
            status_code=500,
            detail="Não foi possível coletar dados da Hemominas"
        )

    hemocentro = db.query(Hemocentro).filter(
        Hemocentro.nome == "Hemominas",
        Hemocentro.estado == "MG"
    ).first()

    if not hemocentro:
        hemocentro = Hemocentro(
            nome="Hemominas",
            estado="MG",
            cidade="Belo Horizonte",
            site="https://www.hemominas.mg.gov.br"
        )

        db.add(hemocentro)
        db.commit()
        db.refresh(hemocentro)

    atualizados = 0
    criados = 0

    for tipo, status in dados.items():
        estoque = db.query(Estoque).filter(
            Estoque.hemocentro_id == hemocentro.id,
            Estoque.tipo_sanguineo == tipo
        ).first()

        if estoque:
            estoque.status = status
            estoque.fonte = "Hemominas"
            estoque.ultima_atualizacao = datetime.now()
            atualizados += 1
        else:
            novo = Estoque(
                hemocentro_id=hemocentro.id,
                tipo_sanguineo=tipo,
                status=status,
                fonte="Hemominas",
                ultima_atualizacao=datetime.now()
            )

            db.add(novo)
            criados += 1

    db.commit()

    return {
        "sucesso": True,
        "fonte": "Hemominas",
        "estoques_coletados": dados,
        "registros_criados": criados,
        "registros_atualizados": atualizados
    }