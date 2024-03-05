""" Fábricas para la creación de objetos del dominio de localizaciones

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de localizaciones

"""

from .entidades import Localizacion
from .reglas import UbicacionNoVacio
from .excepciones import TipoObjetoNoExisteEnDominioLocalizacionesExcepcion
from propdalpescoleccioncomp.seedwork.dominio.repositorios import Mapeador, Repositorio
from propdalpescoleccioncomp.seedwork.dominio.fabricas import Fabrica
from propdalpescoleccioncomp.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaLocalizacion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            localizacion: Localizacion = mapeador.dto_a_entidad(obj)
            

            self.validar_regla(UbicacionNoVacio(localizacion.ubicacion))
            
            return localizacion

@dataclass
class FabricaLocalizaciones(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Localizacion.__class__:
            fabrica_localizacion = _FabricaLocalizacion()
            return fabrica_localizacion.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioLocalizacionesExcepcion()

