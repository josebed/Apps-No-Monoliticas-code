import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from flask import session
import asyncio
import requests

from propdalpescoleccioncomp.modulos.companias.infraestructura.schema.v1.eventos import EventoCompaniaCreada
from propdalpescoleccioncomp.modulos.companias.infraestructura.schema.v1.comandos import ComandoCrearCompania
from propdalpescoleccioncomp.seedwork.aplicacion.comandos import ejecutar_commando
from propdalpescoleccioncomp.modulos.companias.aplicacion.comandos.crear_compania import CrearCompania, ejecutar_comando_crear_compania
from propdalpescoleccioncomp.seedwork.infraestructura import utils
import propdalpescoleccioncomp.api.companias as api

_FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

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
            
            external_api_url = 'http://localhost:5000/companias/compania-comando2'
            json_data = locacion_a_dict(comando)
            response = requests.post(external_api_url, json=json_data)

            if response.status_code == 200:
                # Parse the JSON response
                print("paso")
            else:
                # If the request was not successful, return an error message
                print("fallo")
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def locacion_a_dict(locacion):
        if not locacion:
            return dict(fecha_creacion=None, fecha_actualizacion=None, id=None, nombre=None, numero=None, tipo=None)
        
        return dict(
                    fecha_creacion=locacion.fecha_creacion
                ,   fecha_actualizacion=locacion.fecha_actualizacion
                ,    id=locacion.id
                ,   nombre=locacion.nombre
                ,   numero=locacion.numero
                ,   tipo=locacion.tipo
        )
