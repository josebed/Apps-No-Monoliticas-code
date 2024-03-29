""" Excepciones del dominio de companias

En este archivo usted encontrará los Excepciones relacionadas
al dominio de companias

"""

from consolidacionCompania.seedwork.dominio.excepciones import ExcepcionFabrica


class TipoObjetoNoExisteEnDominioConsolidacionExcepcion(ExcepcionFabrica):
    def __init__(
        self,
        mensaje="No existe una fábrica para el tipo solicitado en el módulo de consolidacion",
    ):
        self.__mensaje = mensaje

    def __str__(self):
        return str(self.__mensaje)
