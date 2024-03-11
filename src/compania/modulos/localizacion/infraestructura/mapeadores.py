""" Mapeadores para la capa de infrastructura del dominio de companias

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from compania.seedwork.dominio.repositorios import Mapeador
from compania.modulos.localizacion.dominio.entidades import Localizacion
from .dto import Localizacion as LocalizacionDTO


class MapeadorLocalizacion(Mapeador):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"

    def obtener_tipo(self) -> type:
        return Localizacion.__class__

    def entidad_a_dto(self, entidad: Localizacion) -> LocalizacionDTO:

        localizacion_dto = LocalizacionDTO()
        localizacion_dto.fecha_creacion = entidad.fecha_creacion
        localizacion_dto.fecha_actualizacion = entidad.fecha_actualizacion
        localizacion_dto.id = str(entidad.id)
        localizacion_dto.ubicacion = entidad.ubicacion
        localizacion_dto.ciudad = entidad.ciudad
        localizacion_dto.numero = entidad.numero
        localizacion_dto.latitud = entidad.latitud
        localizacion_dto.longitud = entidad.longitud

        return localizacion_dto

    def dto_a_entidad(self, dto: LocalizacionDTO) -> Localizacion:
        localizacion = Localizacion(
            dto.id,
            dto.fecha_creacion,
            dto.fecha_actualizacion,
            dto.ubicacion,
            dto.ciudad,
            dto.numero,
            dto.latitud,
            dto.longitud,
        )

        return localizacion
