from pydantic import BaseModel
from typing import Optional


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