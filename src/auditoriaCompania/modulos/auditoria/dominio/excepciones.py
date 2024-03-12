""" Excepciones del dominio de auditoria

En este archivo usted encontrará los Excepciones relacionadas
al dominio de auditoria

"""

from auditoriaCompania.seedwork.dominio.excepciones import ExcepcionFabrica


class TipoObjetoNoExisteEnDominioAuditoriaExcepcion(ExcepcionFabrica):
    def __init__(
        self,
        mensaje="No existe una fábrica para el tipo solicitado en el módulo de auditoria",
    ):
        self.__mensaje = mensaje

    def __str__(self):
        return str(self.__mensaje)
