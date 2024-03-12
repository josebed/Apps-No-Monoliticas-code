from pydispatch import dispatcher

from .handlers import HandlerConsolidacionIntegracion

from consolidacionCompania.modulos.consolidacion.dominio.eventos import (
    CompaniaConsolidada,
)
from consolidacionCompania.modulos.consolidacion.aplicacion.comandos.consolidacion_compania import (
    ConsolidarCompania,
)

dispatcher.connect(
    HandlerConsolidacionIntegracion.handle_compania_consolidada,
    signal=f"{CompaniaConsolidada.__name__}Integracion",
)
dispatcher.connect(
    HandlerConsolidacionIntegracion.handle_compania_consolidada_comando,
    signal=f"{ConsolidarCompania.__name__}Integracion",
)
