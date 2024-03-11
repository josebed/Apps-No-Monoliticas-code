from compania.seedwork.aplicacion.handlers import Handler
from compania.modulos.companias.infraestructura.despachadores import Despachador


class HandlerCompaniaIntegracion(Handler):

    @staticmethod
    def handle_compania_creada_comando(comando):
        despachador = Despachador()
        despachador.publicar_comando(comando, "comandos-compania")

    @staticmethod
    def handle_compania_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, "eventos-compania")
