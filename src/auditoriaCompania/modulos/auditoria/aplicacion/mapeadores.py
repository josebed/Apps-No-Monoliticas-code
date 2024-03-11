from auditoriaCompania.seedwork.aplicacion.dto import Mapeador as AppMap
from auditoriaCompania.seedwork.dominio.repositorios import Mapeador as RepMap
from auditoriaCompania.modulos.auditoria.dominio.entidades import Auditoria
from .dto import AuditoriaDTO

from datetime import datetime


class MapeadorAuditoriaDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> AuditoriaDTO:
        auditoria_dto = AuditoriaDTO(
            "",
            "",
            "",
            externo.get("compania", str),
            externo.get("fecha", str),
            externo.get("descripcion", str),
        )

        return auditoria_dto

    def dto_a_externo(self, dto: AuditoriaDTO) -> dict:
        return dto.__dict__


class MapeadorAuditoria(RepMap):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"

    def obtener_tipo(self) -> type:
        return Auditoria.__class__

    def locacion_a_dict(self, locacion):
        if not locacion:
            return dict(
                codigo=None, nombre=None, fecha_actualizacion=None, fecha_creacion=None
            )

        return dict(
            codigo=locacion.codigo,
            nombre=locacion.nombre,
            fecha_actualizacion=locacion.fecha_actualizacion.strftime(
                self._FORMATO_FECHA
            ),
            fecha_creacion=locacion.fecha_creacion.strftime(self._FORMATO_FECHA),
        )

    def entidad_a_dto(self, entidad: Auditoria) -> AuditoriaDTO:

        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)

        return AuditoriaDTO(
            fecha_creacion,
            fecha_actualizacion,
            _id,
            entidad.compania,
            entidad.fecha,
            entidad.descripcion,
        )

    def dto_a_entidad(self, dto: AuditoriaDTO) -> Auditoria:
        auditoria = Auditoria(
            id_compania=dto.compania, fecha=dto.fecha, descripcion=dto.descripcion
        )

        return auditoria
