"""Reglas de negocio del dominio de cliente

En este archivo usted encontrará reglas de negocio del dominio de cliente

"""

from propdalpescoleccioncomp.seedwork.dominio.reglas import ReglaNegocio
from .entidades import Locacion
from .objetos_valor import InformacionGeoespacial

class UbicacionNoVacio(ReglaNegocio):

    ubicacion: InformacionGeoespacial

    def __init__(self, ubicacion, mensaje='El campo ubicacion no puede estar vacio.'):
        super().__init__(mensaje)
        self.ubicacion = ubicacion

    def es_valido(self) -> bool:
        if self.ubicacion:
            return True
        else:
            return False
