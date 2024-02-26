from propdalpescoleccioncomp.config.db import db
from propdalpescoleccioncomp.modulos.companias.dominio.repositorios import RepositorioCompanias
from propdalpescoleccioncomp.modulos.companias.dominio.entidades import Compania
from propdalpescoleccioncomp.modulos.companias.dominio.fabricas import FabricaCompanias
from .dto import Compania as CompaniaDTO
from .mapeadores import MapeadorCompania
from uuid import UUID

class RepositorioCompaniasSQLite(RepositorioCompanias):

    def __init__(self):
        self._fabrica_companias: FabricaCompanias = FabricaCompanias()

    @property
    def fabrica_companias(self):
        return self._fabrica_companias

    def obtener_por_id(self, id: UUID) -> Compania:
        compania_dto = db.session.query(CompaniaDTO).filter_by(id=str(id)).one()
        return self.fabrica_companias.crear_objeto(compania_dto, MapeadorCompania())

    def obtener_todos(self) -> list[Compania]:
        # TODO
        raise NotImplementedError

    def agregar(self, compania: Compania):
        compania_dto = self.fabrica_companias.crear_objeto(compania, MapeadorCompania())
        print(compania_dto.nombre)
        db.session.add(compania_dto)
        db.session.commit() # quitar al pasar a eventos

    def actualizar(self, compania: Compania):
        # TODO
        raise NotImplementedError

    def eliminar(self, compania_id: UUID):
        # TODO
        raise NotImplementedError