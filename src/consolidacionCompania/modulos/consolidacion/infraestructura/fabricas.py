from dataclasses import dataclass, field
from consolidacionCompania.seedwork.dominio.fabricas import Fabrica
from consolidacionCompania.seedwork.dominio.repositorios import Repositorio
from consolidacionCompania.modulos.consolidacion.dominio.repositorios import (
    RepositorioConsolidacion,
)
from .repositorios import RepositorioConsolidacionSQLite
from .excepciones import ExcepcionFabrica


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioConsolidacion.__class__:
            return RepositorioConsolidacionSQLite()
        else:
            raise ExcepcionFabrica()
