from consolidacionCompania.seedwork.aplicacion.queries import QueryHandler
from consolidacionCompania.modulos.consolidacion.infraestructura.fabricas import (
    FabricaRepositorio,
)
from consolidacionCompania.modulos.consolidacion.dominio.fabricas import (
    FabricaConsolidacion,
)


class ConsolidacionQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_consolidacion: FabricaConsolidacion = FabricaConsolidacion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_consolidacion(self):
        return self._fabrica_consolidacion
