from consolidacionCompania.seedwork.aplicacion.handlers import Handler
from consolidacionCompania.modulos.consolidacion.infraestructura.despachadores import (
    Despachador,
)


class HandlerConsolidacionIntegracion(Handler):

    @staticmethod
    def handle_compania_consolidada_comando(comando):
        despachador = Despachador()
        despachador.publicar_comando(comando, "comandos-consolidacion")

    @staticmethod
    def handle_compania_consolidada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, "eventos-consolidacion")
