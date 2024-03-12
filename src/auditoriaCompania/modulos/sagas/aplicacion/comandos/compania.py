from pulsar.schema import *
from dataclasses import dataclass, field
from auditoriaCompania.seedwork.infraestructura.schema.v1.comandos import (
    ComandoIntegracion,
)

class AuditarCompania: 
    fecha_creacion = String()
    fecha_actualizacion = String()
    id_compania = String()
    compania = String()
    numero = String()
    tipo = String()


class RevertirAuditoria: ...


class CrearCompania: ...


class HabilitarVisualizacionCompania: ...