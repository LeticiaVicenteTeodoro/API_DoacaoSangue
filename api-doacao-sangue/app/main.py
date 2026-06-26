from fastapi import FastAPI

from app.routes import hemocentros, estoques, campanhas, compatibilidade, cidades
from app.database import criar_tabelas, popular_dados_iniciais

app = FastAPI(
    title="API Aberta de Doação de Sangue",
    description="API para integração, padronização e disponibilização de dados sobre doação de sangue.",
    version="1.0.0"
)

criar_tabelas()
popular_dados_iniciais()

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
