from consolidacionCompania.seedwork.aplicacion.queries import (
    Query,
    QueryHandler,
    QueryResultado,
)
from consolidacionCompania.seedwork.aplicacion.queries import (
    ejecutar_query as query,
)
from consolidacionCompania.modulos.consolidacion.infraestructura.repositorios import (
    RepositorioConsolidacion,
)
from dataclasses import dataclass
from .base import ConsolidacionQueryBaseHandler
from consolidacionCompania.modulos.consolidacion.aplicacion.mapeadores import (
    MapeadorConsolidacion,
)
import uuid


@dataclass
class ObtenerConsolidacion(Query):
    id: str


class ObtenerConsolidacionHandler(ConsolidacionQueryBaseHandler):

    def handle(self, query: ObtenerConsolidacion) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioConsolidacion.__class__
        )
        reserva = self.fabrica_consolidacion.crear_objeto(
            repositorio.obtener_por_id(query.id), MapeadorConsolidacion()
        )
        return QueryResultado(resultado=reserva)


@query.register(ObtenerConsolidacion)
def ejecutar_query_obtener_consolidacion(query: ObtenerConsolidacion):
    handler = ObtenerConsolidacionHandler()
    return handler.handle(query)
