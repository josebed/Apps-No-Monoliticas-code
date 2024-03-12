from pulsar.schema import *
from dataclasses import dataclass, field
from auditoriaCompania.seedwork.infraestructura.schema.v1.comandos import (
    ComandoIntegracion,
)


class ComandoAuditarCompaniaPayload(Record):
    fecha_creacion = String()
    fecha_actualizacion = String()
    id = String()
    compania = String()
    fecha = String()
    descripcion = String()


class ComandoAuditarCompania(ComandoIntegracion):
    data = ComandoAuditarCompaniaPayload()
