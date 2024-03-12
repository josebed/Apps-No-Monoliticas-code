""" Mapeadores para la capa de infrastructura del dominio de companias

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from consolidacionCompania.seedwork.dominio.repositorios import Mapeador
from consolidacionCompania.modulos.companias.dominio.entidades import Compania
from .dto import Compania as CompaniaDTO


class MapeadorCompania(Mapeador):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"

    def obtener_tipo(self) -> type:
        return Compania.__class__

    def entidad_a_dto(self, entidad: Compania) -> CompaniaDTO:

        compania_dto = CompaniaDTO()
        compania_dto.fecha_creacion = entidad.fecha_creacion
        compania_dto.fecha_actualizacion = entidad.fecha_actualizacion
        compania_dto.id = str(entidad.id)
        compania_dto.nombre = entidad.nombre
        compania_dto.numero = entidad.numero
        compania_dto.tipo = entidad.tipo

        return compania_dto

    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        compania = Compania(
            id=dto.id,
            fecha_creacion=dto.fecha_creacion,
            fecha_actualizacion=dto.fecha_actualizacion,
            nombre=dto.nombre,
            numero=dto.numero,
            tipo=dto.tipo,
        )

        return compania
