from dataclasses import dataclass, field
from auditoria.seedwork.dominio.fabricas import Fabrica
from auditoria.seedwork.dominio.repositorios import Repositorio
from auditoria.modulos.auditoria.dominio.repositorios import RepositorioAuditoria
from .repositorios import RepositorioAuditoriaSQLite
from .excepciones import ExcepcionFabrica


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioAuditoria.__class__:
            return RepositorioAuditoriaSQLite()
        else:
            raise ExcepcionFabrica()
