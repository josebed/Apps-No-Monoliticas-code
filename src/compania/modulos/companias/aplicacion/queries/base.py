from propdalpescoleccioncomp.seedwork.aplicacion.queries import QueryHandler
from propdalpescoleccioncomp.modulos.companias.infraestructura.fabricas import FabricaRepositorio
from propdalpescoleccioncomp.modulos.companias.dominio.fabricas import FabricaCompanias

class CompaniasQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_companias: FabricaCompanias = FabricaCompanias()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_companias(self):
        return self._fabrica_companias    