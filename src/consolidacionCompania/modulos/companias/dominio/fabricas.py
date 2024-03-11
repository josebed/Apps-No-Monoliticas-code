""" Fábricas para la creación de objetos del dominio de companias

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de companias

"""

from .entidades import Compania
from .reglas import NombreCompNoVacio
from .excepciones import TipoObjetoNoExisteEnDominioCompaniasExcepcion
from propdalpesconsolidacioncomp.seedwork.dominio.repositorios import (
    Mapeador,
    Repositorio,
)
from propdalpesconsolidacioncomp.seedwork.dominio.fabricas import Fabrica
from propdalpesconsolidacioncomp.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass


@dataclass
class _FabricaCompania(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            compania: Compania = mapeador.dto_a_entidad(obj)

            self.validar_regla(NombreCompNoVacio(compania.nombre))

            return compania


@dataclass
class FabricaCompanias(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Compania.__class__:
            fabrica_compania = _FabricaCompania()
            return fabrica_compania.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioCompaniasExcepcion()
