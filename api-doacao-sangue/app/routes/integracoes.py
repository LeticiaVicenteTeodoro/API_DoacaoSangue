from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import get_db
from app.models import Hemocentro, Estoque
from app.services.hemominas import coletar_estoque_hemominas
from app.services.hemosc import coletar_estoque_hemosc
from app.services.hemepar import coletar_estoque_hemepar
from app.services.hemoes import coletar_estoque_hemoes
from app.services.hemoce import coletar_estoque_hemoce
from app.services.hemopa import coletar_estoque_hemopa

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

@router.post("/hemosc/estoques")
def atualizar_estoque_hemosc(
    db: Session = Depends(get_db)
):
    dados = coletar_estoque_hemosc()

    if not dados:
        raise HTTPException(
            status_code=500,
            detail="Não foi possível coletar dados do HEMOSC"
        )

    hemocentro = db.query(Hemocentro).filter(
        Hemocentro.nome == "HEMOSC",
        Hemocentro.estado == "SC"
    ).first()

    if not hemocentro:
        hemocentro = Hemocentro(
            nome="HEMOSC",
            estado="SC",
            cidade="Florianópolis",
            site="https://www.hemosc.org.br"
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
            estoque.fonte = "HEMOSC"
            estoque.ultima_atualizacao = datetime.now()
            atualizados += 1
        else:
            novo = Estoque(
                hemocentro_id=hemocentro.id,
                tipo_sanguineo=tipo,
                status=status,
                fonte="HEMOSC",
                ultima_atualizacao=datetime.now()
            )

            db.add(novo)
            criados += 1

    db.commit()

    return {
        "sucesso": True,
        "fonte": "HEMOSC",
        "estoques_coletados": dados,
        "registros_criados": criados,
        "registros_atualizados": atualizados
    }


@router.post("/hemepar/estoques")
def atualizar_estoque_hemepar(
    db: Session = Depends(get_db)
):
    dados = coletar_estoque_hemepar()

    if not dados:
        raise HTTPException(
            status_code=500,
            detail="Não foi possível coletar dados do HEMEPAR"
        )

    hemocentro = db.query(Hemocentro).filter(
        Hemocentro.nome == "HEMEPAR",
        Hemocentro.estado == "PR"
    ).first()

    if not hemocentro:
        hemocentro = Hemocentro(
            nome="HEMEPAR",
            estado="PR",
            cidade="Curitiba",
            site="https://www.saude.pr.gov.br/Pagina/Hemepar-Centro-de-Hematologia-e-Hemoterapia-do-Parana"
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
            estoque.fonte = "HEMEPAR"
            estoque.ultima_atualizacao = datetime.now()

            atualizados += 1

        else:

            novo = Estoque(
                hemocentro_id=hemocentro.id,
                tipo_sanguineo=tipo,
                status=status,
                fonte="HEMEPAR",
                ultima_atualizacao=datetime.now()
            )

            db.add(novo)

            criados += 1

    db.commit()

    return {
        "sucesso": True,
        "fonte": "HEMEPAR",
        "estoques_coletados": dados,
        "registros_criados": criados,
        "registros_atualizados": atualizados
    }

@router.post("/hemoes/estoques")
def atualizar_estoque_hemoes(
    db: Session = Depends(get_db)
):
    dados = coletar_estoque_hemoes()

    if not dados:
        raise HTTPException(
            status_code=500,
            detail="Não foi possível coletar dados do HEMOES"
        )

    hemocentro = db.query(Hemocentro).filter(
        Hemocentro.nome == "HEMOES",
        Hemocentro.estado == "ES"
    ).first()

    if not hemocentro:
        hemocentro = Hemocentro(
            nome="HEMOES",
            estado="ES",
            cidade="Vitória",
            site="https://hemoes.es.gov.br/"
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
            estoque.fonte = "HEMOES"
            estoque.ultima_atualizacao = datetime.now()
            atualizados += 1
        else:
            novo = Estoque(
                hemocentro_id=hemocentro.id,
                tipo_sanguineo=tipo,
                status=status,
                fonte="HEMOES",
                ultima_atualizacao=datetime.now()
            )

            db.add(novo)
            criados += 1

    db.commit()

    return {
        "sucesso": True,
        "fonte": "HEMOES",
        "estoques_coletados": dados,
        "registros_criados": criados,
        "registros_atualizados": atualizados
    }

@router.post("/hemoce/estoques")
def atualizar_estoque_hemoce(
    db: Session = Depends(get_db)
):
    dados = coletar_estoque_hemoce()

    if not dados:
        raise HTTPException(
            status_code=500,
            detail="Não foi possível coletar dados do HEMOCE"
        )

    hemocentro = db.query(Hemocentro).filter(
        Hemocentro.nome == "HEMOCE",
        Hemocentro.estado == "CE"
    ).first()

    if not hemocentro:
        hemocentro = Hemocentro(
            nome="HEMOCE",
            estado="CE",
            cidade="Fortaleza",
            site="https://www.hemoce.ce.gov.br/"
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
            estoque.fonte = "HEMOCE"
            estoque.ultima_atualizacao = datetime.now()
            atualizados += 1
        else:
            novo = Estoque(
                hemocentro_id=hemocentro.id,
                tipo_sanguineo=tipo,
                status=status,
                fonte="HEMOCE",
                ultima_atualizacao=datetime.now()
            )

            db.add(novo)
            criados += 1

    db.commit()

    return {
        "sucesso": True,
        "fonte": "HEMOCE",
        "estoques_coletados": dados,
        "registros_criados": criados,
        "registros_atualizados": atualizados
    }

@router.post("/hemopa/estoques")
def atualizar_estoque_hemopa(
    db: Session = Depends(get_db)
):
    dados = coletar_estoque_hemopa()

    if not dados:
        raise HTTPException(
            status_code=500,
            detail="Não foi possível coletar dados do HEMOPA"
        )

    hemocentro = db.query(Hemocentro).filter(
        Hemocentro.nome == "HEMOPA",
        Hemocentro.estado == "PA"
    ).first()

    if not hemocentro:
        hemocentro = Hemocentro(
            nome="HEMOPA",
            estado="PA",
            cidade="Belém",
            site="https://www.hemopa.pa.gov.br/"
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
            estoque.fonte = "HEMOPA"
            estoque.ultima_atualizacao = datetime.now()
            atualizados += 1
        else:
            novo = Estoque(
                hemocentro_id=hemocentro.id,
                tipo_sanguineo=tipo,
                status=status,
                fonte="HEMOPA",
                ultima_atualizacao=datetime.now()
            )

            db.add(novo)
            criados += 1

    db.commit()

    return {
        "sucesso": True,
        "fonte": "HEMOPA",
        "estoques_coletados": dados,
        "registros_criados": criados,
        "registros_atualizados": atualizados
    }