# API Aberta de Doação de Sangue

Projeto inicial para TCC: desenvolvimento de uma API aberta para integração, padronização e disponibilização de dados sobre doação de sangue.

## Tecnologias

- Python
- FastAPI
- SQLite
- Uvicorn

## Como rodar

### 1. Criar ambiente virtual

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Rodar a API

```bash
uvicorn app.main:app --reload
```

### 4. Abrir documentação

Acesse:

```text
http://127.0.0.1:8000/docs
```

## Endpoints iniciais

```text
GET /
GET /hemocentros
GET /hemocentros/proximos
GET /estoques
GET /estoques/criticos
GET /campanhas
GET /campanhas/ativas
GET /compatibilidade/{tipo}
GET /cidades
GET /cidades/{estado}
```

## Objetivo acadêmico

A API busca reduzir a fragmentação de dados relacionados à doação de sangue, oferecendo uma estrutura padronizada que possa ser consumida por aplicativos, sistemas web, pesquisadores e instituições.
