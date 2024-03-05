from auditoria.seedwork.aplicacion.comandos import Comando
from auditoria.modulos.auditoria.aplicacion.dto import AuditoriaDTO
from .base import AuditarCompaniaBaseHandler
from dataclasses import dataclass, field
from auditoria.seedwork.aplicacion.comandos import ejecutar_commando as comando
from auditoria.seedwork.aplicacion.comandos import despachar_commando as descomando

from auditoria.modulos.auditoria.dominio.entidades import Auditoria
from auditoria.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from auditoria.modulos.auditoria.aplicacion.mapeadores import MapeadorAuditoria
from auditoria.modulos.auditoria.infraestructura.repositorios import (
    RepositorioAuditoria,
)
from pydispatch import dispatcher
from flask import session


@dataclass
class AuditarCompania(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    compania: str
    fecha: str
    descripcion: str


class AuditarCompaniaHandler(AuditarCompaniaBaseHandler):

    def handle(self, comando: AuditarCompania):
        print("AUDITANDO COMP HANDLE")
        auditoria_dto = AuditoriaDTO(
            fecha_actualizacion=comando.fecha_actualizacion,
            fecha_creacion=comando.fecha_creacion,
            id=comando.id,
            compania=comando.compania,
            fecha=comando.fecha,
            descripcion=comando.descripcion,
        )

        print("AUDITANDO COMP HANDLE 2 ")
        print(auditoria_dto)

        auditoria: Auditoria = self.fabrica_auditoria.crear_objeto(
            auditoria_dto, MapeadorAuditoria()
        )

        print("AUDITANDO COMP CREAR  ")
        print(auditoria)
        auditoria.auditar_compania(auditoria)

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioAuditoria.__class__
        )

        print("AUDITANDO COMP REPO  ")
        print(repositorio)
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, auditoria)
        print("AUDITANDO COMP BATCH  ")
        UnidadTrabajoPuerto.savepoint()
        print("AUDITANDO COMP SAVE  ")
        UnidadTrabajoPuerto.commit()
        print("AUDITANDO COMP COMMIT  ")


@comando.register(AuditarCompania)
def ejecutar_comando_auditar_compania(comando: AuditarCompania):
    print("AUDITANDO COMP")
    handler = AuditarCompaniaHandler()
    handler.handle(comando)


@descomando.register(AuditarCompania)
def despachar_comando_auditar_compania(comando: AuditarCompania):
    dispatcher.send(signal=f"{type(comando).__name__}Integracion", comando=comando)
