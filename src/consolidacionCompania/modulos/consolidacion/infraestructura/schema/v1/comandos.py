from pulsar.schema import *
from dataclasses import dataclass, field
from compania.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion


class ComandoConsolidarCompaniaPayload(Record):
    fecha_creacion = String()
    fecha_actualizacion = String()
    id = String()
    nombre = String()
    numero = String()
    tipo = String()


class ComandoConsolidarCompania(ComandoIntegracion):
    data = ComandoConsolidarCompaniaPayload()
