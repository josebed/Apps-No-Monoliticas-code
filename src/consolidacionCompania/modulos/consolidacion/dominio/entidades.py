from __future__ import annotations
from dataclasses import dataclass, field

import consolidacionCompania.modulos.consolidacion.dominio.objetos_valor as ov
from consolidacionCompania.modulos.consolidacion.dominio.eventos import (
    CompaniaConsolidada,
)
from consolidacionCompania.seedwork.dominio.entidades import (
    Locacion,
    AgregacionRaiz,
    Entidad,
)


@dataclass
class Consolidacion(AgregacionRaiz):
    id_localizacion: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoConsolidacion = field(default=ov.EstadoConsolidacion.PENDIENTE)
    nombre: ov.NombreComp = field(default_factory=ov.NombreComp)
    numero: ov.DocumentoIdentidad = field(default_factory=ov.DocumentoIdentidad)
    tipo: ov.TipoIndustria = field(default_factory=ov.TipoIndustria)

    def consolidar_compania(self, consolidacion: Consolidacion):
        self.id_localizacion = consolidacion.id_localizacion
        self.estado = consolidacion.estado
        self.nombre = consolidacion.nombre
        self.numero = consolidacion.numero
        self.tipo = consolidacion.tipo

        self.agregar_evento(
            CompaniaConsolidada(
                id_compania=self.id,
                id_localizacion=self.id_localizacion,
                estado=self.estado.name,
                fecha_creacion=self.fecha_creacion,
            )
        )
