""" Interfaces para los repositorios del dominio de localizaciones

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de localizaciones

"""

from abc import ABC
from propdalpescoleccioncomp.seedwork.dominio.repositorios import Repositorio

class RepositorioLocalizaciones(Repositorio, ABC):
    ...
    