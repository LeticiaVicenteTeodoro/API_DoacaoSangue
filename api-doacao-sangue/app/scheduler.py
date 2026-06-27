from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import SessionLocal
from app.routes.integracoes import (
    atualizar_estoque_hemominas,
    atualizar_estoque_hemosc,
    atualizar_estoque_hemepar,
)


scheduler = BackgroundScheduler()


def executar_atualizacao(nome, funcao):
    db: Session = SessionLocal()

    try:
        print(f"[{datetime.now()}] Atualizando {nome}...")
        resultado = funcao(db)
        print(f"[{datetime.now()}] {nome} atualizado:", resultado)

    except Exception as e:
        print(f"[{datetime.now()}] ERRO ao atualizar {nome}:", e)

    finally:
        db.close()


def iniciar_scheduler():
    if scheduler.running:
        return

    scheduler.add_job(
        executar_atualizacao,
        "cron",
        hour=9,
        minute=0,
        args=["Hemominas", atualizar_estoque_hemominas],
    )

    scheduler.add_job(
        executar_atualizacao,
        "cron",
        hour=10,
        minute=0,
        args=["HEMOSC", atualizar_estoque_hemosc],
    )

    scheduler.add_job(
        executar_atualizacao,
        "cron",
        hour=11,
        minute=0,
        args=["HEMEPAR", atualizar_estoque_hemepar],
    )

    scheduler.start()
    print("Scheduler iniciado.")