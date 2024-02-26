from pulsar.schema import *
from aeroalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ReservaCreadaPayload(Record):
    id_reserva = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoReservaCreada(EventoIntegracion):
    data = ReservaCreadaPayload()