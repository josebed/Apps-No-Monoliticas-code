from compania.config.db import db
from compania.modulos.locallizacion.dominio.repositorios import (
    RepositorioLocalizaciones,
)
from compania.modulos.locallizacion.dominio.entidades import Localizacion
from compania.modulos.locallizacion.dominio.fabricas import FabricaLocalizaciones
from .dto import Localizacion as LocalizacionDTO
from .mapeadores import MapeadorLocalizacion
from uuid import UUID


class RepositorioLocalizacionesSQLite(RepositorioLocalizaciones):

    def __init__(self):
        self._fabrica_localizaciones: FabricaLocalizaciones = FabricaLocalizaciones()

    @property
    def fabrica_localizaciones(self):
        return self._fabrica_localizaciones

    def obtener_por_id(self, id: UUID) -> Localizacion:
        localizacion_dto = db.session.query(LocalizacionDTO).filter_by(id=str(id)).one()
        return self.fabrica_localizaciones.crear_objeto(
            localizacion_dto, MapeadorLocalizacion()
        )

    def obtener_todos(self) -> list[Localizacion]:
        # TODO
        raise NotImplementedError

    def agregar(self, localizacion: Localizacion):
        localizacion_dto = self.fabrica_localizaciones.crear_objeto(
            localizacion, MapeadorLocalizacion()
        )
        db.session.add(localizacion_dto)
        db.session.commit()  # quitar al pasar a eventos

    def actualizar(self, localizacion: Localizacion):
        # TODO
        raise NotImplementedError

    def eliminar(self, localizacion_id: UUID):
        # TODO
        raise NotImplementedError
