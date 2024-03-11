from auditoriaCompania.seedwork.aplicacion.handlers import Handler
from auditoriaCompania.modulos.auditoria.infraestructura.despachadores import (
    Despachador,
)


class HandlerAuditoriaIntegracion(Handler):

    @staticmethod
    def handle_compania_auditada_comando(comando):
        despachador = Despachador()
        despachador.publicar_comando(comando, "comandos-auditoria")

    @staticmethod
    def handle_compania_auditada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, "eventos-auditoria")
