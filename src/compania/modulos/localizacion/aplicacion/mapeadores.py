from compania.seedwork.aplicacion.dto import Mapeador as AppMap
from compania.seedwork.dominio.repositorios import Mapeador as RepMap
from compania.modulos.locallizacion.dominio.entidades import Localizacion
from .dto import LocalizacionDTO

from datetime import datetime


class MapeadorLocalizacionDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> LocalizacionDTO:
        localizacion_dto = LocalizacionDTO(
            "",
            "",
            "",
            externo.get("ubicacion", str),
            externo.get("ciudad", str),
            externo.get("numero", str),
            externo.get("latitud", str),
            externo.get("longitud", str),
        )

        return localizacion_dto

    def dto_a_externo(self, dto: LocalizacionDTO) -> dict:
        return dto.__dict__


class MapeadorLocalizacion(RepMap):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"

    def obtener_tipo(self) -> type:
        return Localizacion.__class__

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

    def entidad_a_dto(self, entidad: Localizacion) -> LocalizacionDTO:

        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        # itinerarios = list()

        # for itin in entidad.itinerarios:
        #     odos = list()
        #     for odo in itin.odos:
        #         segmentos = list()
        #         for seg in odo.segmentos:
        #             legs = list()
        #             for leg in seg.legs:
        #                 fecha_salida = leg.fecha_salida.strftime(self._FORMATO_FECHA)
        #                 fecha_llegada = leg.fecha_llegada.strftime(self._FORMATO_FECHA)
        #                 origen = self.locacion_a_dict(leg.origen)
        #                 destino = self.locacion_a_dict(leg.destino)
        #                 leg = LegDTO(fecha_salida=fecha_salida, fecha_llegada=fecha_llegada, origen=origen, destino=destino)

        #                 legs.append(leg)

        #             segmentos.append(SegmentoDTO(legs))
        #         odos.append(OdoDTO(segmentos))
        #     itinerarios.append(ItinerarioDTO(odos))

        return LocalizacionDTO(
            fecha_creacion,
            fecha_actualizacion,
            _id,
            entidad.ubicacion,
            entidad.ciudad,
            entidad.numero,
            entidad.latitud,
            entidad.longitud,
        )

    def dto_a_entidad(self, dto: LocalizacionDTO) -> Localizacion:
        localizacion = Localizacion(
            ubicacion=dto.ubicacion,
            ciudad=dto.ciudad,
            numero=dto.numero,
            latitud=dto.latitud,
            longitud=dto.longitud,
        )

        return localizacion
