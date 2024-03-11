import pulsar
from pulsar.schema import *

from auditoria.modulos.auditoria.infraestructura.schema.v1.eventos import (
    EventoCompaniaAuditada,
    CompaniaAuditadaPayload,
)
from auditoria.modulos.auditoria.infraestructura.schema.v1.comandos import (
    ComandoAuditarCompania,
    ComandoAuditarCompaniaPayload,
)
from auditoria.seedwork.infraestructura import utils

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
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = CompaniaAuditadaPayload(
            id_audtoria=str(evento.id_auditoria),
            id_compania=str(evento.id_compania),
            fecha=str(evento.fecha),
            descripcion=str(evento.descripcion),
        )
        evento_integracion = EventoCompaniaAuditada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, EventoCompaniaAuditada)

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        print("PUBLICAR COMANDO")
        payload = ComandoAuditarCompaniaPayload(
            fecha_creacion=str(comando.fecha_creacion),
            fecha_actualizacion=str(comando.fecha_actualizacion),
            id=str(comando.id),
            fecha=str(comando.fecha),
            descripcion=str(comando.descripcion),
        )
        print("PUBLICADO")
        print(payload)
        comando_integracion = ComandoAuditarCompania(data=payload)
        self._publicar_mensaje(comando_integracion, topico, ComandoAuditarCompania)
