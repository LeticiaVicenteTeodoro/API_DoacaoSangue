# API Aberta de Doação de Sangue

API REST para integração, padronização e disponibilização de dados sobre doação de sangue no Brasil.

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Selenium
- BeautifulSoup
- APScheduler

## Funcionalidades

- CRUD de hemocentros
- CRUD de estoques
- CRUD de campanhas
- CRUD de fontes de dados
- Compatibilidade sanguínea
- Integração com Hemominas MG
- Integração com HEMOSC SC
- Integração com HEMEPAR PR
- Endpoint nacional de estoques
- Scheduler para atualização automática

## Como executar

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload