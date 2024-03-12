from __future__ import annotations

from dataclasses import dataclass, field
from compania.seedwork.dominio.objetos_valor import ObjetoValor, Codigo, Ruta, Locacion
from datetime import datetime
from enum import Enum


@dataclass(frozen=True)
class NombreComp:
    nombre: str


@dataclass(frozen=True)
class DocumentoIdentidad(ObjetoValor):
    numero: str


@dataclass(frozen=True)
class TipoIndustria(ObjetoValor):
    tipo: str


class EstadoCompania(str, Enum):
    APROBADA = "Aprobada"
    PENDIENTE = "Pendiente"
    CANCELADA = "Cancelada"
    PAGADA = "Pagada"
