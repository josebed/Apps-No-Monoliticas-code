import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


COMPANIA_HOST = os.getenv("AEROALPES_ADDRESS", default="localhost")

def obtener_companias(root) -> typing.List["Compania"]:
    companias_json = requests.get(f'http://{COMPANIA_HOST}:5000/companias/compania-query').json()
    companias = []

    for compania in companias_json:
        companias.append(
            compania(
                estado=compania.get('estado'), 
                nombre=compania.get('nombre'), 
                numero=compania.get('numero'), 
                tipo=compania.get('tipo'),
                id=compania.get('id')
            )
        )

    return companias


@strawberry.type
class Compania:
    id: uuid.UUID
    estado: str
    nombre: str
    numero: str
    tipo: str

@strawberry.type
class CompaniaRespuesta:
    mensaje: str
    codigo: int