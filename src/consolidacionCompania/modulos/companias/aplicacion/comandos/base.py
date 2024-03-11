from propdalpesconsolidacioncomp.seedwork.aplicacion.comandos import ComandoHandler
from propdalpesconsolidacioncomp.modulos.companias.infraestructura.fabricas import (
    FabricaRepositorio,
)
from propdalpesconsolidacioncomp.modulos.companias.dominio.fabricas import (
    FabricaCompanias,
)


class CrearCompaniaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_companias: FabricaCompanias = FabricaCompanias()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_companias(self):
        return self._fabrica_companias
