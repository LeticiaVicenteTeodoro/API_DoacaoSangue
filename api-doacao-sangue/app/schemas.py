from pydantic import BaseModel
from typing import Optional


class HemocentroSchema(BaseModel):
    id: int
    nome: str
    cidade: str
    estado: str
    endereco: Optional[str] = None
    telefone: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    fonte: Optional[str] = None


class EstoqueSchema(BaseModel):
    id: int
    estado: str
    cidade: Optional[str] = None
    fonte: str
    tipo_sanguineo: str
    status: str
    ultima_atualizacao: Optional[str] = None


class CampanhaSchema(BaseModel):
    id: int
    titulo: str
    cidade: Optional[str] = None
    estado: Optional[str] = None
    descricao: Optional[str] = None
    data_inicio: Optional[str] = None
    data_fim: Optional[str] = None
    fonte: Optional[str] = None
