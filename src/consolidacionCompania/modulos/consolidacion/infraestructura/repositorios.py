from consolidacionCompania.config.db import db
from consolidacionCompania.modulos.consolidacion.dominio.repositorios import (
    RepositorioConsolidacion,
)
from consolidacionCompania.modulos.consolidacion.dominio.entidades import Consolidacion
from consolidacionCompania.modulos.consolidacion.dominio.fabricas import (
    FabricaConsolidacion,
)
from .dto import Consolidacion as ConsolidacionDTO
from .mapeadores import MapeadorConsolidacion
from uuid import UUID


class RepositorioConsolidacionSQLite(RepositorioConsolidacion):

    def __init__(self):
        self._fabrica_consolidacion: FabricaConsolidacion = FabricaConsolidacion()

    @property
    def fabrica_consolidacion(self):
        return self._fabrica_consolidacion

    def obtener_por_id(self, id: UUID) -> Consolidacion:
        consolidacion_dto = (
            db.session.query(ConsolidacionDTO).filter_by(id=str(id)).one()
        )
        return self.fabrica_consolidacion.crear_objeto(
            consolidacion_dto, MapeadorConsolidacion()
        )

    def obtener_todos(self) -> list[Consolidacion]:
        # TODO
        raise NotImplementedError

    def agregar(self, consolidacion: Consolidacion):
        consolidacion_dto = self.fabrica_consolidacion.crear_objeto(
            consolidacion, MapeadorConsolidacion()
        )
        print(consolidacion_dto.nombre)
        db.session.add(consolidacion_dto)
        db.session.commit()

    def actualizar(self, consolidacion: Consolidacion):
        raise NotImplementedError

    def eliminar(self, consolidacion_id: UUID):
        raise NotImplementedError
