from pulsar.schema import *
from auditoriaCompania.seedwork.infraestructura.schema.v1.eventos import (
    EventoIntegracion,
)

from dataclasses import dataclass, field
from auditoriaCompania.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class CompaniaAuditadaPayload(Record):
    id_auditoria = String()
    id_compania = String()
    fecha = String()
    descripcion = String()


class EventoCompaniaAuditada(EventoIntegracion):
    data = CompaniaAuditadaPayload()


class CompaniaCreadaPayload(Record):
    id_compania = String()
    id_localizacion = String()
    estado = String()
    fecha_creacion = Long()


class EventoCompaniaCreada(EventoIntegracion):
    data = CompaniaCreadaPayload()


class EventoCompania(EventoDominio):
    ...

class CompaniaCreada(EventoCompania):
    id_compania:str = None
    id_localizacion:str = None
    estado:str = None
    fecha_creacion:datetime = None