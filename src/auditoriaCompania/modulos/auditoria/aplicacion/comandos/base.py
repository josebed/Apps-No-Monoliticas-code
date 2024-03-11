from auditoria.seedwork.aplicacion.comandos import ComandoHandler
from auditoria.modulos.auditoria.infraestructura.fabricas import FabricaRepositorio
from auditoria.modulos.auditoria.dominio.fabricas import FabricaAuditoria

class AuditarCompaniaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_auditoria: FabricaAuditoria = FabricaAuditoria()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_auditoria(self):
        return self._fabrica_auditoria    
    