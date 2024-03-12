import consolidacionCompania.seedwork.presentacion.api as api
import json, time
import asyncio

from consolidacionCompania.seedwork.dominio.excepciones import ExcepcionDominio
from flask import redirect, render_template, request, session, url_for
from flask import Response

from consolidacionCompania.modulos.companias.aplicacion.servicios import (
    ServicioCompania,
)
from consolidacionCompania.modulos.companias.aplicacion.mapeadores import (
    MapeadorCompaniaDTOJson,
)
from consolidacionCompania.modulos.companias.aplicacion.comandos.crear_compania import (
    CrearCompania,
)
from consolidacionCompania.modulos.companias.aplicacion.queries.obtener_compania import (
    ObtenerCompania,
)

from consolidacionCompania.seedwork.aplicacion.comandos import ejecutar_commando
from consolidacionCompania.seedwork.aplicacion.comandos import despachar_commando
from consolidacionCompania.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint("companias", "/companias")


@bp.route("/compania", methods=("POST",))
def crear():
    try:
        crear_dict = request.json

        map_compania = MapeadorCompaniaDTOJson()
        compania_dto = map_compania.externo_a_dto(crear_dict)

        sr = ServicioCompania()
        dto_final = sr.crear_compania(compania_dto)

        return map_compania.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(
            json.dumps(dict(error=str(e))), status=400, mimetype="application/json"
        )


@bp.route("/compania-comando", methods=("POST",))
async def crear_asincrona():
    try:
        session.clear()

        crear_dict = request.json

        map_compania = MapeadorCompaniaDTOJson()
        compania_dto = map_compania.externo_a_dto(crear_dict)

        comando = CrearCompania(
            compania_dto.fecha_creacion,
            compania_dto.fecha_actualizacion,
            compania_dto.id,
            compania_dto.nombre,
            compania_dto.numero,
            compania_dto.tipo,
        )

        task = asyncio.create_task(ejecutar_comando_async(comando))
        despachar_commando(comando)
        await task

        return Response("{}", status=202, mimetype="application/json")
    except ExcepcionDominio as e:
        return Response(
            json.dumps(dict(error=str(e))), status=400, mimetype="application/json"
        )


@bp.route("/compania", methods=("GET",))
@bp.route("/compania/<id>", methods=("GET",))
def dar_compania(id=None):
    if id:
        sr = ServicioCompania()
        map_compania = MapeadorCompaniaDTOJson()

        return map_compania.dto_a_externo(sr.obtener_compania_por_id(id))
    else:
        return [{"message": "GET!"}]


@bp.route("/compania-query", methods=("GET",))
@bp.route("/compania-query/<id>", methods=("GET",))
def dar_compania_usando_query(id=None, region: str = ""):
    if id:
        region = request.args.get("region")
        query_resultado = ejecutar_query(ObtenerCompania(id))
        map_compania = MapeadorCompaniaDTOJson()
        return map_compania.dto_a_externo(query_resultado.resultado, region)
    else:
        return [{"message": "GET!"}]


async def ejecutar_comando_async(comando):
    ejecutar_commando(comando)
