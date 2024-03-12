""" Interfaces para los repositorios del dominio de companias

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de companias

"""

from abc import ABC
from compania.seedwork.dominio.repositorios import Repositorio


class RepositorioCompanias(Repositorio, ABC): ...
