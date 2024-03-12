from consolidacionCompania.seedwork.aplicacion.servicios import Servicio
from consolidacionCompania.modulos.companias.dominio.entidades import Compania
from consolidacionCompania.modulos.companias.dominio.fabricas import (
    FabricaCompanias,
)
from consolidacionCompania.modulos.companias.infraestructura.fabricas import (
    FabricaRepositorio,
)
from consolidacionCompania.modulos.companias.infraestructura.repositorios import (
    RepositorioCompanias,
)
from consolidacionCompania.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .mapeadores import MapeadorCompania

from .dto import CompaniaDTO


class ServicioCompania(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_companias: FabricaCompanias = FabricaCompanias()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_companias(self):
        return self._fabrica_companias

    def crear_compania(self, compania_dto: CompaniaDTO) -> CompaniaDTO:
        compania: Compania = self.fabrica_companias.crear_objeto(
            compania_dto, MapeadorCompania()
        )
        compania.crear_compania(compania)

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioCompanias.__class__
        )

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, compania)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return self.fabrica_companias.crear_objeto(compania, MapeadorCompania())

    def obtener_compania_por_id(self, id) -> CompaniaDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioCompanias.__class__
        )
        return self.fabrica_companias.crear_objeto(
            repositorio.obtener_por_id(id), MapeadorCompania()
        )
