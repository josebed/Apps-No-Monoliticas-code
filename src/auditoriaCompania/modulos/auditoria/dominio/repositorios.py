""" Interfaces para los repositorios del dominio de auditoria

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de auditoria

"""

from abc import ABC
from auditoriaCompania.seedwork.dominio.repositorios import Repositorio


class RepositorioAuditoria(Repositorio, ABC): ...
