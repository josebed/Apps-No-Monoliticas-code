from propdalpescoleccioncomp.seedwork.aplicacion.comandos import ComandoHandler
from propdalpescoleccioncomp.modulos.vuelos.infraestructura.fabricas import FabricaRepositorio
from propdalpescoleccioncomp.modulos.vuelos.dominio.fabricas import FabricaVuelos

class CrearReservaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_vuelos: FabricaVuelos = FabricaVuelos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos    
    