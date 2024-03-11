from dataclasses import dataclass, field
from compania.seedwork.dominio.fabricas import Fabrica
from compania.seedwork.dominio.repositorios import Repositorio
from compania.modulos.companias.dominio.repositorios import RepositorioCompanias
from .repositorios import RepositorioCompaniasSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioCompanias.__class__:
            return RepositorioCompaniasSQLite()
        else:
            raise ExcepcionFabrica()