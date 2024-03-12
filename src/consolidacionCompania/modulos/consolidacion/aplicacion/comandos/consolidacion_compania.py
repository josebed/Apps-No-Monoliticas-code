from consolidacionCompania.seedwork.aplicacion.comandos import Comando
from consolidacionCompania.modulos.consolidacion.aplicacion.dto import ConsolidacionDTO
from .base import ConsolidarCompaniaBaseHandler
from dataclasses import dataclass, field
from consolidacionCompania.seedwork.aplicacion.comandos import (
    ejecutar_commando as comando,
)
from consolidacionCompania.seedwork.aplicacion.comandos import (
    despachar_commando as descomando,
)

from consolidacionCompania.modulos.consolidacion.dominio.entidades import Consolidacion
from consolidacionCompania.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from consolidacionCompania.modulos.consolidacion.aplicacion.mapeadores import (
    MapeadorConsolidacion,
)
from consolidacionCompania.modulos.consolidacion.infraestructura.repositorios import (
    RepositorioConsolidacion,
)
from pydispatch import dispatcher
from flask import session


@dataclass
class ConsolidarCompania(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    nombre: str
    numero: str
    tipo: str


class ConsolidarCompaniaHandler(ConsolidarCompaniaBaseHandler):

    def handle(self, comando: ConsolidarCompania):
        consolidacion_dto = ConsolidacionDTO(
            fecha_actualizacion=comando.fecha_actualizacion,
            fecha_creacion=comando.fecha_creacion,
            id=comando.id,
            nombre=comando.nombre,
            numero=comando.numero,
            tipo=comando.tipo,
        )

        consolidacion: Consolidacion = self.fabrica_consolidacion.crear_objeto(
            consolidacion_dto, MapeadorConsolidacion()
        )
        consolidacion.consolidar_compania(consolidacion)

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioConsolidacion.__class__
        )
        print("aqui llego")
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, consolidacion)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(ConsolidarCompania)
def ejecutar_comando_crear_compania(comando: ConsolidarCompania):
    handler = ConsolidarCompaniaHandler()
    handler.handle(comando)


@descomando.register(ConsolidarCompania)
def despachar_comando_crear_compania(comando: ConsolidarCompania):
    dispatcher.send(signal=f"{type(comando).__name__}Integracion", comando=comando)
