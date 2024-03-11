from __future__ import annotations

from dataclasses import dataclass, field
from compania.seedwork.dominio.objetos_valor import ObjetoValor, Codigo, Ruta, Locacion
from datetime import datetime
from enum import Enum


@dataclass(frozen=True)
class Direccion(ObjetoValor):
    ciudad: str
    numero: str


@dataclass(frozen=True)
class InformacionGeoespacial(ObjetoValor):
    ubicacion: str


@dataclass(frozen=True)
class DatosGeograficos(ObjetoValor):
    latitud: str
    longitud: str
