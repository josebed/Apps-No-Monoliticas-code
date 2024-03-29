import pulsar
from pulsar.schema import *

from consolidacionCompania.modulos.consolidacion.infraestructura.schema.v1.eventos import (
    EventoCompaniaConsolidada,
    CompaniaConsolidadaPayload,
)
from consolidacionCompania.modulos.consolidacion.infraestructura.schema.v1.comandos import (
    ComandoConsolidarCompania,
    ComandoConsolidarCompaniaPayload,
)
from consolidacionCompania.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f"pulsar://{utils.broker_host()}:6650")
        publicador = cliente.create_producer(topico, schema=AvroSchema(schema))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = CompaniaConsolidadaPayload(
            id_compania=str(evento.id_compania),
            id_localizacion=str(evento.id_localizacion),
            estado=str(evento.estado),
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion)),
        )
        evento_integracion = EventoCompaniaConsolidada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, EventoCompaniaConsolidada)

    def publicar_comando(self, comando, topico):
        payload = ComandoConsolidarCompaniaPayload(
            fecha_creacion=str(comando.fecha_creacion),
            fecha_actualizacion=str(comando.fecha_actualizacion),
            id=str(comando.id),
            nombre=str(comando.nombre),
            numero=str(comando.numero),
            tipo=str(comando.tipo),
        )
        comando_integracion = ComandoConsolidarCompania(data=payload)
        self._publicar_mensaje(comando_integracion, topico, ComandoConsolidarCompania)
