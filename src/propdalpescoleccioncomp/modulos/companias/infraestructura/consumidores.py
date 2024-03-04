import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from flask import session

from propdalpescoleccioncomp.modulos.companias.infraestructura.schema.v1.eventos import EventoCompaniaCreada
from propdalpescoleccioncomp.modulos.companias.infraestructura.schema.v1.comandos import ComandoCrearCompania
from propdalpescoleccioncomp.seedwork.aplicacion.comandos import ejecutar_commando
from propdalpescoleccioncomp.modulos.companias.aplicacion.comandos.crear_compania import CrearCompania, ejecutar_comando_crear_compania
from propdalpescoleccioncomp.seedwork.infraestructura import utils
import propdalpescoleccioncomp.api.companias as api

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-compania', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propdalpescoleccioncomp-sub-eventos', schema=AvroSchema(EventoCompaniaCreada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None

    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-compania', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='propdalpescoleccioncomp-sub-comandos', schema=AvroSchema(ComandoCrearCompania))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)  

            comando = CrearCompania(mensaje.value().data.fecha_creacion, 
                                    mensaje.value().data.fecha_actualizacion,
                                    mensaje.value().data.id,
                                    mensaje.value().data.nombre,
                                    mensaje.value().data.numero,
                                    mensaje.value().data.tipo)

            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
