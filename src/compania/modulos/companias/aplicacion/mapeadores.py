from compania.seedwork.aplicacion.dto import Mapeador as AppMap
from compania.seedwork.dominio.repositorios import Mapeador as RepMap
from compania.modulos.companias.dominio.entidades import Compania
from .dto import CompaniaDTO

from datetime import datetime

class MapeadorCompaniaDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> CompaniaDTO:
        compania_dto = CompaniaDTO("","","",externo.get('nombre', str), externo.get('numero', str), externo.get('tipo', str))

        return compania_dto

    def dto_a_externo(self, dto: CompaniaDTO) -> dict:
        return dto.__dict__

class MapeadorCompania(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Compania.__class__

    def locacion_a_dict(self, locacion):
        if not locacion:
            return dict(codigo=None, nombre=None, fecha_actualizacion=None, fecha_creacion=None)
        
        return dict(
                    codigo=locacion.codigo
                ,   nombre=locacion.nombre
                ,   fecha_actualizacion=locacion.fecha_actualizacion.strftime(self._FORMATO_FECHA)
                ,   fecha_creacion=locacion.fecha_creacion.strftime(self._FORMATO_FECHA)
        )
        

    def entidad_a_dto(self, entidad: Compania) -> CompaniaDTO:

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
        
        return CompaniaDTO(fecha_creacion, fecha_actualizacion, _id, entidad.nombre, entidad.numero, entidad.tipo)

    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        compania = Compania(nombre=dto.nombre, numero=dto.numero, tipo=dto.tipo)
        
        return compania



