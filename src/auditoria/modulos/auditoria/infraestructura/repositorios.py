from auditoria.config.db import db
from auditoria.modulos.auditoria.dominio.repositorios import RepositorioAuditoria
from auditoria.modulos.auditoria.dominio.entidades import Auditoria
from auditoria.modulos.auditoria.dominio.fabricas import FabricaAuditoria
from .dto import Auditoria as AuditoriaDTO
from .mapeadores import MapeadorAuditoria
from uuid import UUID


class RepositorioAuditoriaSQLite(RepositorioAuditoria):

    def __init__(self):
        self._fabrica_auditoria: FabricaAuditoria = FabricaAuditoria()

    @property
    def fabrica_auditoria(self):
        return self._fabrica_auditoria

    def obtener_por_id(self, id: UUID) -> Auditoria:
        auditoria_dto = db.session.query(AuditoriaDTO).filter_by(id=str(id)).one()
        return self.fabrica_auditoria.crear_objeto(auditoria_dto, MapeadorAuditoria())

    def obtener_todos(self) -> list[Auditoria]:
        # TODO
        raise NotImplementedError

    def agregar(self, auditoria: Auditoria):
        auditoria_dto = self.fabrica_auditoria.crear_objeto(
            auditoria, MapeadorAuditoria()
        )
        db.session.add(auditoria_dto)

    def actualizar(self, auditoria: Auditoria):
        # TODO
        raise NotImplementedError

    def eliminar(self, auditoria_id: UUID):
        # TODO
        raise NotImplementedError
