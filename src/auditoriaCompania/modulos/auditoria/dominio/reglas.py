"""Reglas de negocio del dominio de cliente

En este archivo usted encontrará reglas de negocio del dominio de cliente

"""

from auditoriaCompania.seedwork.dominio.reglas import ReglaNegocio
from .entidades import Auditoria
from .objetos_valor import Descripcion


class DescCompNoVacio(ReglaNegocio):

    descripcion: Descripcion

    def __init__(
        self, descripcion, mensaje="El campo descripcion no puede estar vacio."
    ):
        super().__init__(mensaje)
        self.descripcion = descripcion

    def es_valido(self) -> bool:
        if self.descripcion:
            return True
        else:
            return False
