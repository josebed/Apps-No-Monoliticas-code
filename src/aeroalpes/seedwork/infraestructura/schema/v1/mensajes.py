import uuid

from pulsar.schema import *
from aeroalpes.seedwork.infraestructura.utils import time_millis

class Mensaje(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()