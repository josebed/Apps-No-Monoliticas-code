from consolidacionCompania.seedwork.aplicacion.dto import Mapeador as AppMap
from consolidacionCompania.seedwork.dominio.repositorios import Mapeador as RepMap
from consolidacionCompania.modulos.consolidacion.dominio.entidades import Consolidacion
from .dto import ConsolidacionDTO
import os
from datetime import datetime


class MapeadorConsolidacionDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> ConsolidacionDTO:
        consolidacion_dto = ConsolidacionDTO(
            "",
            "",
            "",
            externo.get("nombre", str),
            externo.get("numero", str),
            externo.get("tipo", str),
        )

        return consolidacion_dto

    def dto_a_externo(self, dto: ConsolidacionDTO, region: str) -> dict:
        return DTOAExternoInternacinal(region).dto_a_externo(dto)


class MapeadorConsolidacion(RepMap):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"

    def obtener_tipo(self) -> type:
        return Consolidacion.__class__

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

    def entidad_a_dto(self, entidad: Consolidacion) -> ConsolidacionDTO:

        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)

        return ConsolidacionDTO(
            fecha_creacion,
            fecha_actualizacion,
            _id,
            entidad.nombre,
            entidad.numero,
            entidad.tipo,
        )

    def dto_a_entidad(self, dto: ConsolidacionDTO) -> Consolidacion:
        consolidacion = Consolidacion(
            nombre=dto.nombre, numero=dto.numero, tipo=dto.tipo
        )

        return consolidacion


class DTOAExternoInternacinal:
    DEFAULT_REGION = "NA"
    ALLOWED_REGIONS = ["NA", "EU", "SA", "OU"]
    region = DEFAULT_REGION

    def __init__(self, region) -> None:
        if region in self.ALLOWED_REGIONS:
            self.region = region

    def dto_a_externo(self, dto: ConsolidacionDTO) -> dict:
        return self.region_config[self.region](self, dto)

    def na_dto_a_externo(self, dto: ConsolidacionDTO) -> dict:
        return {
            **dto.__dict__,
            "distancia": "millas",
            "area": "pies cuadrados",
            "fecha": "MM-DD-YYYY",
        }

    def eu_sa_dto_a_externo(self, dto: ConsolidacionDTO) -> dict:
        return {
            **dto.__dict__,
            "distancia": "kilometros",
            "area": "metros cuadrados",
            "fecha": "DD-MM-YYYY",
        }

    region_config = {
        "NA": na_dto_a_externo,
        "EU": eu_sa_dto_a_externo,
        "SA": eu_sa_dto_a_externo,
        "OU": eu_sa_dto_a_externo,
    }
