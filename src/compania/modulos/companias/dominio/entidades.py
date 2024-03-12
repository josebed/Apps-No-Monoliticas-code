from __future__ import annotations
from dataclasses import dataclass, field

import compania.modulos.companias.dominio.objetos_valor as ov
from compania.modulos.companias.dominio.eventos import CompaniaCreada
from compania.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad

@dataclass
class Compania(AgregacionRaiz):
    id_localizacion: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoCompania = field(default=ov.EstadoCompania.PENDIENTE)
    nombre: ov.NombreComp = field(default_factory=ov.NombreComp)
    numero: ov.DocumentoIdentidad = field(default_factory=ov.DocumentoIdentidad)
    tipo: ov.TipoIndustria = field(default_factory=ov.TipoIndustria)

    def crear_compania(self, compania: Compania):
        self.id_localizacion = compania.id_localizacion
        self.estado = compania.estado
        self.nombre = compania.nombre
        self.numero = compania.numero
        self.tipo = compania.tipo

        self.agregar_evento(CompaniaCreada(
            id_compania=self.id, 
            nombre=self.nombre,
            numero=self.numero,
            tipo=self.tipo,
            fecha_creacion=self.fecha_creacion))
