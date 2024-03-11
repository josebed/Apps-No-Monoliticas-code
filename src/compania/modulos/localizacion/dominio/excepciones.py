""" Excepciones del dominio de localizaciones

En este archivo usted encontrará los Excepciones relacionadas
al dominio de localizaciones

"""

from compania.seedwork.dominio.excepciones import ExcepcionFabrica


class TipoObjetoNoExisteEnDominioLocalizacionesExcepcion(ExcepcionFabrica):
    def __init__(
        self,
        mensaje="No existe una fábrica para el tipo solicitado en el módulo de localizaciones",
    ):
        self.__mensaje = mensaje

    def __str__(self):
        return str(self.__mensaje)
