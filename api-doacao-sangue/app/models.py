from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    DateTime,
    Boolean,
)
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Hemocentro(Base):
    __tablename__ = "hemocentros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    endereco = Column(String)
    telefone = Column(String)
    site = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)


class Estoque(Base):
    __tablename__ = "estoques"

    id = Column(Integer, primary_key=True, index=True)
    hemocentro_id = Column(Integer, ForeignKey("hemocentros.id"))
    tipo_sanguineo = Column(String, nullable=False)
    status = Column(String, nullable=False)
    fonte = Column(String)
    ultima_atualizacao = Column(DateTime, default=datetime.now)


class Campanha(Base):
    __tablename__ = "campanhas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    estado = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    data_inicio = Column(DateTime)
    data_fim = Column(DateTime)
    ativa = Column(Boolean, default=True)


class FonteDados(Base):
    __tablename__ = "fontes_dados"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    url = Column(String, nullable=False)
    estado = Column(String)
    descricao = Column(String)