from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.scheduler import iniciar_scheduler

from app.routes import hemocentros, estoques, campanhas, compatibilidade, cidades, fontes, integracoes

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Aberta de Doação de Sangue",
    description="API para integração, padronização e disponibilização de dados sobre doação de sangue.",
    version="1.0.0"
)

@app.on_event("startup")
def startup_event():
    iniciar_scheduler()

app.include_router(fontes.router)
app.include_router(integracoes.router)
app.include_router(hemocentros.router)
app.include_router(estoques.router)
app.include_router(campanhas.router)
app.include_router(compatibilidade.router)
app.include_router(cidades.router)


@app.get("/")
def home():
    return {
        "mensagem": "API Doação de Sangue funcionando!",
        "documentacao": "/docs"
    }
