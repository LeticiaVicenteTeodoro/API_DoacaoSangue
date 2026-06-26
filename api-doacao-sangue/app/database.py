import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "banco.db"


def conectar():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def criar_tabelas():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS hemocentros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cidade TEXT NOT NULL,
        estado TEXT NOT NULL,
        endereco TEXT,
        telefone TEXT,
        latitude REAL,
        longitude REAL,
        fonte TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS estoques (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        estado TEXT NOT NULL,
        cidade TEXT,
        fonte TEXT NOT NULL,
        tipo_sanguineo TEXT NOT NULL,
        status TEXT NOT NULL,
        ultima_atualizacao TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS campanhas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        cidade TEXT,
        estado TEXT,
        descricao TEXT,
        data_inicio TEXT,
        data_fim TEXT,
        fonte TEXT
    )
    """)

    conn.commit()
    conn.close()


def popular_dados_iniciais():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) AS total FROM hemocentros")
    total = cur.fetchone()["total"]

    if total == 0:
        cur.execute("""
        INSERT INTO hemocentros
        (nome, cidade, estado, endereco, telefone, latitude, longitude, fonte)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            "Hemominas - Poços de Caldas",
            "Poços de Caldas",
            "MG",
            "Endereço demonstrativo",
            "(35) 0000-0000",
            -21.7878,
            -46.5614,
            "Hemominas"
        ))

        cur.execute("""
        INSERT INTO hemocentros
        (nome, cidade, estado, endereco, telefone, latitude, longitude, fonte)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            "Fundação Pró-Sangue - São Paulo",
            "São Paulo",
            "SP",
            "Endereço demonstrativo",
            "(11) 0000-0000",
            -23.5505,
            -46.6333,
            "Pró-Sangue"
        ))

    cur.execute("SELECT COUNT(*) AS total FROM estoques")
    total_estoques = cur.fetchone()["total"]

    if total_estoques == 0:
        dados = [
            ("MG", "Poços de Caldas", "Hemominas", "O+", "Adequado", "2026-02-01"),
            ("MG", "Poços de Caldas", "Hemominas", "O-", "Crítico", "2026-02-01"),
            ("MG", "Poços de Caldas", "Hemominas", "A+", "Estável", "2026-02-01"),
            ("MG", "Poços de Caldas", "Hemominas", "A-", "Alerta", "2026-02-01"),
            ("SP", "São Paulo", "Pró-Sangue", "O+", "Adequado", "2026-02-01"),
            ("SP", "São Paulo", "Pró-Sangue", "O-", "Alerta", "2026-02-01"),
        ]

        cur.executemany("""
        INSERT INTO estoques
        (estado, cidade, fonte, tipo_sanguineo, status, ultima_atualizacao)
        VALUES (?, ?, ?, ?, ?, ?)
        """, dados)

    cur.execute("SELECT COUNT(*) AS total FROM campanhas")
    total_campanhas = cur.fetchone()["total"]

    if total_campanhas == 0:
        cur.execute("""
        INSERT INTO campanhas
        (titulo, cidade, estado, descricao, data_inicio, data_fim, fonte)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            "Campanha Doe Sangue",
            "Poços de Caldas",
            "MG",
            "Campanha demonstrativa para incentivo à doação de sangue.",
            "2026-02-01",
            "2026-02-28",
            "Hemominas"
        ))

    conn.commit()
    conn.close()
