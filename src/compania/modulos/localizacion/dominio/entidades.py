from __future__ import annotations
from dataclasses import dataclass, field

import compania.modulos.localizacion.dominio.objetos_valor as ov
from compania.modulos.vuelos.dominio.eventos import (
    ReservaCreada,
    ReservaAprobada,
    ReservaCancelada,
    ReservaPagada,
)
from compania.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad


@dataclass
class Localizacion(AgregacionRaiz):
    id_compania: uuid.UUID = field(hash=True, default=None)
    ubicacion: ov.InformacionGeoespacial = field(
        default_factory=ov.InformacionGeoespacial
    )
    ciudad: ov.Direccion = field(default_factory=ov.Direccion)
    numero: ov.Direccion = field(default_factory=ov.Direccion)
    latitud: ov.DatosGeograficos = field(default_factory=ov.DatosGeograficos)
    longitud: ov.DatosGeograficos = field(default_factory=ov.DatosGeograficos)
