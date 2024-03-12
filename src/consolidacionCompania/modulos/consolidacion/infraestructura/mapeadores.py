""" Mapeadores para la capa de infrastructura del dominio de companias

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from consolidacionCompania.seedwork.dominio.repositorios import Mapeador
from consolidacionCompania.modulos.consolidacion.dominio.entidades import Consolidacion
from .dto import Consolidacion as ConsolidacionDTO


class MapeadorConsolidacion(Mapeador):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"

    def obtener_tipo(self) -> type:
        return Consolidacion.__class__

    def entidad_a_dto(self, entidad: Consolidacion) -> ConsolidacionDTO:

        consolidacion_dto = ConsolidacionDTO()
        consolidacion_dto.fecha_creacion = entidad.fecha_creacion
        consolidacion_dto.fecha_actualizacion = entidad.fecha_actualizacion
        consolidacion_dto.id = str(entidad.id)
        consolidacion_dto.nombre = entidad.nombre
        consolidacion_dto.numero = entidad.numero
        consolidacion_dto.tipo = entidad.tipo

        return consolidacion_dto

    def dto_a_entidad(self, dto: ConsolidacionDTO) -> Consolidacion:
        consolidacion = Consolidacion(
            id=dto.id,
            fecha_creacion=dto.fecha_creacion,
            fecha_actualizacion=dto.fecha_actualizacion,
            nombre=dto.nombre,
            numero=dto.numero,
            tipo=dto.tipo,
        )

        return consolidacion
