from dataclasses import dataclass, field
from propdalpescoleccioncomp.seedwork.dominio.fabricas import Fabrica
from propdalpescoleccioncomp.seedwork.dominio.repositorios import Repositorio
from propdalpescoleccioncomp.modulos.locallizacion.dominio.repositorios import RepositorioLocalizaciones
from .repositorios import RepositorioLocalizacionesSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioLocalizaciones.__class__:
            return RepositorioLocalizacionesSQLite()
        else:
            raise ExcepcionFabrica()