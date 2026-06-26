from pydantic import BaseModel
from typing import Optional

from datetime import datetime

class CampanhaBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    estado: str
    cidade: str
    data_inicio: datetime
    data_fim: datetime
    ativa: bool = True


class CampanhaCreate(CampanhaBase):
    pass


class CampanhaUpdate(CampanhaBase):
    pass


class CampanhaResponse(CampanhaBase):
    id: int

    class Config:
        from_attributes = True
        
class EstoqueBase(BaseModel):
    hemocentro_id: int
    tipo_sanguineo: str
    status: str
    fonte: Optional[str] = None


class EstoqueCreate(EstoqueBase):
    pass


class EstoqueUpdate(EstoqueBase):
    pass


class EstoqueResponse(EstoqueBase):
    id: int
    ultima_atualizacao: datetime

    class Config:
        from_attributes = True

class HemocentroBase(BaseModel):
    nome: str
    estado: str
    cidade: str
    endereco: Optional[str] = None
    telefone: Optional[str] = None
    site: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class HemocentroCreate(HemocentroBase):
    pass


class HemocentroUpdate(HemocentroBase):
    pass


class HemocentroResponse(HemocentroBase):
    id: int

    class Config:
        from_attributes = True