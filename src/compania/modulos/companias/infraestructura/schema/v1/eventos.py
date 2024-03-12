from pulsar.schema import *
from compania.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class CompaniaCreadaPayload(Record):
    id_compania = String()
    nombre = String()
    numero = String()
    tipo = String()
    fecha_creacion = Long()


class EventoCompaniaCreada(EventoIntegracion):
    data = CompaniaCreadaPayload()
