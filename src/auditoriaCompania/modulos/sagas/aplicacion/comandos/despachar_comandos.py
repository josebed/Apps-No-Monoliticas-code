from compania.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field
from auditoriaCompania.seedwork.aplicacion.comandos import despachar_commando as desp

from pydispatch import dispatcher


@dataclass
class AuditarCompania(Comando):
    fecha_creacion = str
    fecha_actualizacion = str
    id_compania =str
    compania = str
    numero = str
    tipo = str


@desp.register(AuditarCompania)
def despachar_comando_auditar_compania(comando: AuditarCompania):
    print("llego a despachar el comando")
    dispatcher.send(signal=f"{type(comando).__name__}Integracion", comando=comando)