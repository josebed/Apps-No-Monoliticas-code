"""Reglas de negocio del dominio de cliente

En este archivo usted encontrará reglas de negocio del dominio de cliente

"""

from propdalpesconsolidacioncomp.seedwork.dominio.reglas import ReglaNegocio
from .entidades import Compania
from .objetos_valor import NombreComp


class NombreCompNoVacio(ReglaNegocio):

    nombre: NombreComp

    def __init__(self, nombre, mensaje="El campo nombre no puede estar vacio."):
        super().__init__(mensaje)
        self.nombre = nombre

    def es_valido(self) -> bool:
        if self.nombre:
            return True
        else:
            return False
