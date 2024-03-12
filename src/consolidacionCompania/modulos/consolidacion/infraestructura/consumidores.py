import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from flask import session

from consolidacionCompania.modulos.consolidacion.infraestructura.schema.v1.eventos import (
    EventoCompaniaConsolidada,
)
from consolidacionCompania.modulos.consolidacion.infraestructura.schema.v1.comandos import (
    ComandoConsolidarCompania,
)
from consolidacionCompania.seedwork.aplicacion.comandos import ejecutar_commando
from consolidacionCompania.modulos.consolidacion.aplicacion.comandos.consolidacion_compania import (
    ConsolidarCompania,
)
from consolidacionCompania.seedwork.infraestructura import utils
import consolidacionCompania.api.consolidacion as api


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f"pulsar://{utils.broker_host()}:6650")
        consumidor = cliente.subscribe(
            "eventos-consolidacion",
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name="consolidacionCompania-sub-eventos",
            schema=AvroSchema(EventoCompaniaConsolidada),
        )

        while True:
            mensaje = consumidor.receive()
            print(f"Evento recibido: {mensaje.value().data}")

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error("ERROR: Suscribiendose al tópico de eventos!")
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comandos():
    cliente = None

    try:
        cliente = pulsar.Client(f"pulsar://{utils.broker_host()}:6650")
        consumidor = cliente.subscribe(
            "comandos-consolidacion",
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name="consolidacionCompania-sub-comandos",
            schema=AvroSchema(ComandoConsolidarCompania),
        )

        while True:
            mensaje = consumidor.receive()
            print(f"Comando recibido: {mensaje.value().data}")

            consumidor.acknowledge(mensaje)

            comando = ConsolidarCompania(
                mensaje.value().data.fecha_creacion,
                mensaje.value().data.fecha_actualizacion,
                mensaje.value().data.id,
                mensaje.value().data.nombre,
                mensaje.value().data.numero,
                mensaje.value().data.tipo,
            )

        cliente.close()
    except:
        logging.error("ERROR: Suscribiendose al tópico de comandos!")
        traceback.print_exc()
        if cliente:
            cliente.close()
