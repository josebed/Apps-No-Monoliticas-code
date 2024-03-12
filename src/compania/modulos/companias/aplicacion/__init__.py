from pydispatch import dispatcher

from .handlers import HandlerCompaniaIntegracion

from compania.modulos.companias.dominio.eventos import CompaniaCreada
from compania.modulos.companias.aplicacion.comandos.crear_compania import CrearCompania

dispatcher.connect(
    HandlerCompaniaIntegracion.handle_compania_creada,
    signal=f"{CompaniaCreada.__name__}Integracion",
)
dispatcher.connect(
    HandlerCompaniaIntegracion.handle_compania_creada_comando,
    signal=f"{CrearCompania.__name__}Integracion",
)
