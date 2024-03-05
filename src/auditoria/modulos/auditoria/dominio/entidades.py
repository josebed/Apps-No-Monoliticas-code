from __future__ import annotations
from dataclasses import dataclass, field

import auditoria.modulos.auditoria.dominio.objetos_valor as ov
from auditoria.modulos.auditoria.dominio.eventos import CompaniaAuditada
from auditoria.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad


@dataclass
class Auditoria(AgregacionRaiz):
    id_compania: uuid.UUID = field(hash=True, default=None)
    fecha: ov.Fecha = field(default_factory=ov.Fecha)
    descripcion: ov.Descripcion = field(default_factory=ov.Descripcion)

    def auditar_compania(self, auditoria: Auditoria):
        self.id_compania = auditoria.id_compania
        self.fecha = auditoria.fecha
        self.descripcion = auditoria.descripcion

        self.agregar_evento(
            CompaniaAuditada(
                id_auditoria=self.id,
                id_compania=self.id_compania,
                fecha=self.fecha,
                descripcion=self.descripcion,
            )
        )
