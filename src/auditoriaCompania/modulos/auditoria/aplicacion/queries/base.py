from auditoriaCompania.seedwork.aplicacion.queries import QueryHandler
from auditoriaCompania.modulos.auditoria.infraestructura.fabricas import (
    FabricaRepositorio,
)
from auditoriaCompania.modulos.auditoria.dominio.fabricas import FabricaAuditoria


class AuditoriaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_auditoria: FabricaAuditoria = FabricaAuditoria()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_auditoria(self):
        return self._fabrica_cauditoria
