from __future__ import annotations
from dataclasses import dataclass, field
from compania.seedwork.dominio.eventos import EventoDominio
from datetime import datetime


@dataclass
class CompaniaCreada(EventoDominio):
    id_compania: uuid.UUID = None
    nombre: str = None
    numero: str = None
    tipo: str = None
    fecha_creacion: datetime = None
