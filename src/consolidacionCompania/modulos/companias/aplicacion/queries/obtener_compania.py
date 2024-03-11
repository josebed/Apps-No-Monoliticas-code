from propdalpesconsolidacioncomp.seedwork.aplicacion.queries import (
    Query,
    QueryHandler,
    QueryResultado,
)
from propdalpesconsolidacioncomp.seedwork.aplicacion.queries import (
    ejecutar_query as query,
)
from propdalpesconsolidacioncomp.modulos.companias.infraestructura.repositorios import (
    RepositorioCompanias,
)
from dataclasses import dataclass
from .base import CompaniasQueryBaseHandler
from propdalpesconsolidacioncomp.modulos.companias.aplicacion.mapeadores import (
    MapeadorCompania,
)
import uuid


@dataclass
class ObtenerCompania(Query):
    id: str


class ObtenerCompaniaHandler(CompaniasQueryBaseHandler):

    def handle(self, query: ObtenerCompania) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioCompanias.__class__
        )
        reserva = self.fabrica_companias.crear_objeto(
            repositorio.obtener_por_id(query.id), MapeadorCompania()
        )
        return QueryResultado(resultado=reserva)


@query.register(ObtenerCompania)
def ejecutar_query_obtener_compania(query: ObtenerCompania):
    handler = ObtenerCompaniaHandler()
    return handler.handle(query)
