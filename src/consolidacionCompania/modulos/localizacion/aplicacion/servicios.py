from propdalpescoleccioncomp.seedwork.aplicacion.servicios import Servicio
from propdalpescoleccioncomp.modulos.localizacion.dominio.entidades import Localizacion
from propdalpescoleccioncomp.modulos.localizacion.dominio.fabricas import (
    FabricaLocalizaciones,
)
from propdalpescoleccioncomp.modulos.localizacion.infraestructura.fabricas import (
    FabricaRepositorio,
)
from propdalpescoleccioncomp.modulos.localizacion.infraestructura.repositorios import (
    RepositorioLocalizaciones,
)
from propdalpescoleccioncomp.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .mapeadores import MapeadorLocalizacion

from .dto import LocalizacionDTO

import asyncio


class ServicioLocalizacion(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_localizaciones: FabricaLocalizaciones = FabricaLocalizaciones()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_localizaciones(self):
        return self._fabrica_localizaciones

    def crear_localizacion(self, localizacion_dto: LocalizacionDTO) -> LocalizacionDTO:
        localizacion: Localizacion = self.fabrica_localizaciones.crear_objeto(
            localizacion_dto, MapeadorLocalizacion()
        )

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioLocalizaciones.__class__
        )

        repositorio.agregar(localizacion)

        return self.fabrica_localizaciones.crear_objeto(
            localizacion, MapeadorLocalizacion()
        )

    def obtener_localizacion_por_id(self, id) -> LocalizacionDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioLocalizaciones.__class__
        )
        return self.fabrica_localizaciones.crear_objeto(
            repositorio.obtener_por_id(id), MapeadorLocalizacion()
        )
