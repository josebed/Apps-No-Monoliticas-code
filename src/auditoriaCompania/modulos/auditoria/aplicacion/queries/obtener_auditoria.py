from auditoria.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from auditoria.seedwork.aplicacion.queries import ejecutar_query as query
from auditoria.modulos.auditoria.infraestructura.repositorios import RepositorioAuditoria
from dataclasses import dataclass
from .base import AuditoriaQueryBaseHandler
from auditoria.modulos.auditoria.aplicacion.mapeadores import MapeadorAuditoria
import uuid

@dataclass
class ObtenerAuditoria(Query):
    id: str

class ObtenerAuditoriaHandler(AuditoriaQueryBaseHandler):

    def handle(self, query: ObtenerAuditoria) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAuditoria.__class__)
        reserva =  self.fabrica_auditoria.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorAuditoria())
        return QueryResultado(resultado=reserva)

@query.register(ObtenerAuditoria)
def ejecutar_query_obtener_auditoria(query: ObtenerAuditoria):
    handler = ObtenerAuditoriaHandler()
    return handler.handle(query)