""" Mapeadores para la capa de infrastructura del dominio de auditoria

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from auditoria.seedwork.dominio.repositorios import Mapeador
from auditoria.modulos.auditoria.dominio.entidades import Auditoria
from .dto import Auditoria as AuditoriaDTO


class MapeadorAuditoria(Mapeador):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"

    def obtener_tipo(self) -> type:
        return Auditoria.__class__

    def entidad_a_dto(self, entidad: Auditoria) -> AuditoriaDTO:

        auditoria_dto = AuditoriaDTO()
        auditoria_dto.fecha_creacion = entidad.fecha_creacion
        auditoria_dto.fecha_actualizacion = entidad.fecha_actualizacion
        auditoria_dto.id = str(entidad.id)
        auditoria_dto.compania = entidad.id_compania
        auditoria_dto.fecha = entidad.fecha
        auditoria_dto.descripcion = entidad.descripcion

        return auditoria_dto

    def dto_a_entidad(self, dto: AuditoriaDTO) -> Auditoria:
        print("CREANDO")
        auditoria = Auditoria(
            id=dto.id,
            fecha_creacion=dto.fecha_creacion,
            fecha_actualizacion=dto.fecha_actualizacion,
            id_compania=dto.compania,
            fecha=dto.fecha,
            descripcion=dto.descripcion,
        )
        print("CREO AQUI " + auditoria)

        return auditoria
