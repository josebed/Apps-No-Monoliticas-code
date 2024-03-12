from pydispatch import dispatcher

from .handlers import HandlerAuditoriaIntegracion

from auditoriaCompania.modulos.auditoria.dominio.eventos import CompaniaAuditada
from auditoriaCompania.modulos.sagas.aplicacion.comandos.despachar_comandos import (
    AuditarCompania,
)

dispatcher.connect(
    HandlerAuditoriaIntegracion.handle_compania_auditada,
    signal=f"{CompaniaAuditada.__name__}Integracion",
)
dispatcher.connect(
    HandlerAuditoriaIntegracion.handle_compania_auditada_comando,
    signal=f"{AuditarCompania.__name__}Integracion",
)
