
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    reservas: typing.List[Reserva] = strawberry.field(resolver=obtener_reservas)