from pulsar.schema import *
from auditoriaCompania.seedwork.infraestructura.schema.v1.eventos import (
    EventoIntegracion,
)


class CompaniaAuditadaPayload(Record):
    id_auditoria = String()
    id_compania = String()
    fecha = String()
    descripcion = String()


class EventoCompaniaAuditada(EventoIntegracion):
    data = CompaniaAuditadaPayload()
