from propdalpesconsolidacioncomp.seedwork.aplicacion.comandos import Comando
from propdalpesconsolidacioncomp.modulos.companias.aplicacion.dto import CompaniaDTO
from .base import CrearCompaniaBaseHandler
from dataclasses import dataclass, field
from propdalpesconsolidacioncomp.seedwork.aplicacion.comandos import (
    ejecutar_commando as comando,
)
from propdalpesconsolidacioncomp.seedwork.aplicacion.comandos import (
    despachar_commando as descomando,
)

from propdalpesconsolidacioncomp.modulos.companias.dominio.entidades import Compania
from propdalpesconsolidacioncomp.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from propdalpesconsolidacioncomp.modulos.companias.aplicacion.mapeadores import (
    MapeadorCompania,
)
from propdalpesconsolidacioncomp.modulos.companias.infraestructura.repositorios import (
    RepositorioCompanias,
)
from pydispatch import dispatcher
from flask import session


@dataclass
class CrearCompania(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    nombre: str
    numero: str
    tipo: str


class CrearCompaniaHandler(CrearCompaniaBaseHandler):

    def handle(self, comando: CrearCompania):
        compania_dto = CompaniaDTO(
            fecha_actualizacion=comando.fecha_actualizacion,
            fecha_creacion=comando.fecha_creacion,
            id=comando.id,
            nombre=comando.nombre,
            numero=comando.numero,
            tipo=comando.tipo,
        )

        compania: Compania = self.fabrica_companias.crear_objeto(
            compania_dto, MapeadorCompania()
        )
        compania.crear_compania(compania)

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioCompanias.__class__
        )
        print("aqui llego")
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, compania)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearCompania)
def ejecutar_comando_crear_compania(comando: CrearCompania):
    handler = CrearCompaniaHandler()
    handler.handle(comando)


@descomando.register(CrearCompania)
def despachar_comando_crear_compania(comando: CrearCompania):
    dispatcher.send(signal=f"{type(comando).__name__}Integracion", comando=comando)
