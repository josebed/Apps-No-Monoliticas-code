import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from flask import session

from auditoriaCompania.modulos.auditoria.infraestructura.schema.v1.eventos import (
    EventoCompaniaAuditada, EventoCompaniaCreada
)
from auditoriaCompania.modulos.auditoria.infraestructura.schema.v1.comandos import (
    ComandoAuditarCompania,
)
from auditoriaCompania.seedwork.aplicacion.comandos import ejecutar_commando
from auditoriaCompania.seedwork.aplicacion.eventos import oir_evento
from auditoriaCompania.modulos.sagas.dominio.eventos.compania import CompaniaCreada
from auditoriaCompania.modulos.auditoria.aplicacion.comandos.auditar_compania import (
    AuditarCompania,
    ejecutar_comando_auditar_compania,
)
from auditoriaCompania.seedwork.infraestructura import utils
import auditoriaCompania.api.auditoria as api


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f"pulsar://{utils.broker_host()}:6650")
        consumidor = cliente.subscribe(
            "eventos-auditoria",
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name="auditoria-sub-eventos",
            schema=AvroSchema(EventoCompaniaAuditada),
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


def suscribirse_a_eventos_compania():
    cliente = None
    try:
        cliente = pulsar.Client(f"pulsar://{utils.broker_host()}:6650")
        consumidor = cliente.subscribe(
            "eventos-compania",
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name="propdalpescoleccioncomp-sub-eventos",
            schema=AvroSchema(EventoCompaniaCreada),
        )

        while True:
            mensaje = consumidor.receive()
            print(f"Evento recibido: {mensaje.value().data}")

            datos = mensaje.value().data
            consumidor.acknowledge(mensaje)

            print(datos.id_compania)

            compania_creada = CompaniaCreada(
                id=datos.id_compania
            )
            compania_creada.nombre = datos.nombre
            compania_creada.numero = datos.numero
            compania_creada.tipo = datos.tipo
            compania_creada.fecha_creacion = datos.fecha_creacion

            oir_evento(compania_creada)

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
            "comandos-auditoria",
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name="auditoria-sub-comandos",
            schema=AvroSchema(ComandoAuditarCompania),
        )

        while True:
            mensaje = consumidor.receive()
            print(f"Comando recibido: {mensaje.value().data}")

            consumidor.acknowledge(mensaje)

            comando = AuditarCompania(
                mensaje.value().data.fecha_creacion,
                mensaje.value().data.fecha_actualizacion,
                mensaje.value().data.id,
                mensaje.value().data.compania,
                mensaje.value().data.fecha,
                mensaje.value().data.descripcion,
            )

        cliente.close()
    except:
        logging.error("ERROR: Suscribiendose al tópico de comandos!")
        traceback.print_exc()
        if cliente:
            cliente.close()
