""" Excepciones para la capa de infrastructura del dominio de auditoria

En este archivo usted encontrará los Excepciones relacionadas
a la capa de infraestructura del dominio de auditoria

"""

from auditoriaCompania.seedwork.dominio.excepciones import ExcepcionFabrica


class NoExisteImplementacionParaTipoFabricaExcepcion(ExcepcionFabrica):
    def __init__(
        self,
        mensaje="No existe una implementación para el repositorio con el tipo dado.",
    ):
        self.__mensaje = mensaje

    def __str__(self):
        return str(self.__mensaje)
