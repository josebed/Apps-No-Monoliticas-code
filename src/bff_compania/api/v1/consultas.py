
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    companias: typing.List[Compania] = strawberry.field(resolver=obtener_companias)