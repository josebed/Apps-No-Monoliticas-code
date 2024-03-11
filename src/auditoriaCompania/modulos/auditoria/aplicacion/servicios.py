from auditoria.seedwork.aplicacion.servicios import Servicio
from auditoria.modulos.auditoria.dominio.entidades import Auditoria
from auditoria.modulos.auditoria.dominio.fabricas import FabricaAuditoria
from auditoria.modulos.auditoria.infraestructura.fabricas import FabricaRepositorio
from auditoria.modulos.auditoria.infraestructura.repositorios import RepositorioAuditoria
from auditoria.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .mapeadores import MapeadorAuditoria

from .dto import AuditoriaDTO

import asyncio

class ServicioAuditoria(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_auditoria: FabricaAuditoria = FabricaAuditoria()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_auditoria(self):
        return self._fabrica_auditoria       
    
    def auditar_compania(self, auditoria_dto: AuditoriaDTO) -> AuditoriaDTO:
        auditoria: Auditoria = self.fabrica_auditoria.crear_objeto(auditoria_dto, MapeadorAuditoria())
        auditoria.auditar_compania(auditoria)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAuditoria.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, auditoria)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        # repositorio.agregar(auditoria) # quitar al pasar a eventos

        return self.fabrica_auditoria.crear_objeto(auditoria, MapeadorAuditoria())

    def obtener_auditoria_por_id(self, id) -> AuditoriaDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAuditoria.__class__)
        return self.fabrica_auditoria.crear_objeto(repositorio.obtener_por_id(id), MapeadorAuditoria())

