from pulsar.schema import *
from dataclasses import dataclass, field
from propdalpescoleccioncomp.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearCompaniaPayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records para itinerarios

class ComandoCrearCompania(ComandoIntegracion):
    data = ComandoCrearCompaniaPayload()