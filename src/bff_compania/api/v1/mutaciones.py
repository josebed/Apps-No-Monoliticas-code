import strawberry
import typing

from strawberry.types import Info
from bff_compania import utils
from bff_compania.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def crear_compania(self, nombre: str, numero: str, tipo: str, info: Info) -> CompaniaRespuesta:
        print(f"nombre: {nombre}, numero: {numero}, tipo {tipo}")

        comando = dict(
            fecha_creacion= str(datetime.now()),
            fecha_actualizacion= str(datetime.now()),
            id = str(uuid.uuid4()),
            nombre = nombre,
            numero = numero,
            tipo = tipo
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comandos-compania", "public/default/comandos-compania")
        
        return CompaniaRespuesta(mensaje="Procesando Mensaje", codigo=203)