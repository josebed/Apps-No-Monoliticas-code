""" Fábricas para la creación de objetos del dominio de auditoria

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de auditoria

"""

from .entidades import Auditoria
from .reglas import DescCompNoVacio
from .excepciones import TipoObjetoNoExisteEnDominioAuditoriaExcepcion
from auditoria.seedwork.dominio.repositorios import Mapeador, Repositorio
from auditoria.seedwork.dominio.fabricas import Fabrica
from auditoria.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaAuditoria(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            auditoria: Auditoria = mapeador.dto_a_entidad(obj)

            self.validar_regla(DescCompNoVacio(auditoria.descripcion))
            
            return auditoria

@dataclass
class FabricaAuditoria(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Auditoria.__class__:
            fabrica_auditoria = _FabricaAuditoria()
            return fabrica_auditoria.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioAuditoriaExcepcion()

