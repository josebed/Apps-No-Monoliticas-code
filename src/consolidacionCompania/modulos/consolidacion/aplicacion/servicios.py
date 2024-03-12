from consolidacionCompania.seedwork.aplicacion.servicios import Servicio
from consolidacionCompania.modulos.consolidacion.dominio.entidades import Consolidacion
from consolidacionCompania.modulos.consolidacion.dominio.fabricas import (
    FabricaConsolidacion,
)
from consolidacionCompania.modulos.consolidacion.infraestructura.fabricas import (
    FabricaRepositorio,
)
from consolidacionCompania.modulos.consolidacion.infraestructura.repositorios import (
    RepositorioConsolidacion,
)
from consolidacionCompania.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .mapeadores import MapeadorConsolidacion

from .dto import ConsolidacionDTO


class ServicioConsolidacion(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_consolidacion: FabricaConsolidacion = FabricaConsolidacion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_consolidacion(self):
        return self._fabrica_consolidacion

    def consolidar_compania(
        self, consolidacion_dto: ConsolidacionDTO
    ) -> ConsolidacionDTO:
        consolidacion: Consolidacion = self.fabrica_consolidacion.crear_objeto(
            consolidacion_dto, MapeadorConsolidacion()
        )
        consolidacion.consolidar_compania(consolidacion)

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioConsolidacion.__class__
        )

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, consolidacion)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return self.fabrica_consolidacion.crear_objeto(
            consolidacion, MapeadorConsolidacion()
        )

    def obtener_consolidacion_por_id(self, id) -> ConsolidacionDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioConsolidacion.__class__
        )
        return self.fabrica_consolidacion.crear_objeto(
            repositorio.obtener_por_id(id), MapeadorConsolidacion()
        )
