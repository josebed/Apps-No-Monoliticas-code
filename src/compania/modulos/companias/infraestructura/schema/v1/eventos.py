from pulsar.schema import *
from propdalpescoleccioncomp.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class CompaniaCreadaPayload(Record):
    id_compania = String()
    id_localizacion = String()
    estado = String()
    fecha_creacion = Long()

class EventoCompaniaCreada(EventoIntegracion):
    data = CompaniaCreadaPayload()