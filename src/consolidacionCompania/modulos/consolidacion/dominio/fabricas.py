""" Fábricas para la creación de objetos del dominio de companias

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de companias

"""

from .entidades import Consolidacion
from .reglas import NombreCompNoVacio
from .excepciones import TipoObjetoNoExisteEnDominioConsolidacionExcepcion
from consolidacionCompania.seedwork.dominio.repositorios import (
    Mapeador,
    Repositorio,
)
from consolidacionCompania.seedwork.dominio.fabricas import Fabrica
from consolidacionCompania.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass


@dataclass
class _FabricaConsolidacion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            consolidacion: Consolidacion = mapeador.dto_a_entidad(obj)

            self.validar_regla(NombreCompNoVacio(consolidacion.nombre))

            return consolidacion


@dataclass
class FabricaConsolidacion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Consolidacion.__class__:
            fabrica_consolidacion = _FabricaConsolidacion()
            return fabrica_consolidacion.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioConsolidacionExcepcion()
