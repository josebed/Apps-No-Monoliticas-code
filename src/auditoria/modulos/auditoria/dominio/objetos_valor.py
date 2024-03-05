from __future__ import annotations

from dataclasses import dataclass, field
from auditoria.seedwork.dominio.objetos_valor import ObjetoValor, Codigo, Ruta, Locacion
from datetime import datetime
from enum import Enum

@dataclass(frozen=True)
class Descripcion():
    descripcion: str

@dataclass(frozen=True)
class Fecha(ObjetoValor):
    fecha: str

@dataclass(frozen=True)
class Compania(ObjetoValor):
    compania: str

