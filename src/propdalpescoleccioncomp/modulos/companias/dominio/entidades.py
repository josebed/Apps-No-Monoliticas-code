from __future__ import annotations
from dataclasses import dataclass, field

import propdalpescoleccioncomp.modulos.companias.dominio.objetos_valor as ov
from propdalpescoleccioncomp.modulos.vuelos.dominio.eventos import ReservaCreada, ReservaAprobada, ReservaCancelada, ReservaPagada
from propdalpescoleccioncomp.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad

@dataclass
class Compania(AgregacionRaiz):
    id_compania: uuid.UUID = field(hash=True, default=None)
    nombre: ov.NombreComp = field(default_factory=ov.NombreComp)
    numero: ov.DocumentoIdentidad = field(default_factory=ov.DocumentoIdentidad)
    tipo: ov.TipoIndustria = field(default_factory=ov.TipoIndustria)
