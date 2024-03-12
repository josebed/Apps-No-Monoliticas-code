import consolidacionCompania.seedwork.presentacion.api as api
import json, time
import asyncio

from consolidacionCompania.seedwork.dominio.excepciones import ExcepcionDominio
from flask import redirect, render_template, request, session, url_for
from flask import Response

from consolidacionCompania.modulos.consolidacion.aplicacion.servicios import (
    ServicioConsolidacion,
)
from consolidacionCompania.modulos.consolidacion.aplicacion.mapeadores import (
    MapeadorConsolidacionDTOJson,
)
from consolidacionCompania.modulos.consolidacion.aplicacion.comandos.consolidacion_compania import (
    ConsolidarCompania,
)
from consolidacionCompania.modulos.consolidacion.aplicacion.queries.obtener_consolidacion import (
    ObtenerConsolidacion,
)

from consolidacionCompania.seedwork.aplicacion.comandos import ejecutar_commando
from consolidacionCompania.seedwork.aplicacion.comandos import despachar_commando
from consolidacionCompania.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint("consolidacion", "/consolidacion")


@bp.route("/consolidacion", methods=("POST",))
def crear():
    try:
        crear_dict = request.json

        map_consolidacion = MapeadorConsolidacionDTOJson()
        consolidacion_dto = map_consolidacion.externo_a_dto(crear_dict)

        sr = ServicioConsolidacion()
        dto_final = sr.consolidar_compania(consolidacion_dto)

        return map_consolidacion.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(
            json.dumps(dict(error=str(e))), status=400, mimetype="application/json"
        )


@bp.route("/consolidacion-comando", methods=("POST",))
async def crear_asincrona():
    try:
        session.clear()

        crear_dict = request.json

        map_consolidacion = MapeadorConsolidacionDTOJson()
        consolidacion_dto = map_consolidacion.externo_a_dto(crear_dict)

        comando = ConsolidarCompania(
            consolidacion_dto.fecha_creacion,
            consolidacion_dto.fecha_actualizacion,
            consolidacion_dto.id,
            consolidacion_dto.nombre,
            consolidacion_dto.numero,
            consolidacion_dto.tipo,
        )

        task = asyncio.create_task(ejecutar_comando_async(comando))
        despachar_commando(comando)
        await task

        return Response("{}", status=202, mimetype="application/json")
    except ExcepcionDominio as e:
        return Response(
            json.dumps(dict(error=str(e))), status=400, mimetype="application/json"
        )


@bp.route("/consolidacion", methods=("GET",))
@bp.route("/consolidacion/<id>", methods=("GET",))
def dar_consolidacion(id=None):
    if id:
        sr = ServicioConsolidacion()
        map_consolidacion = MapeadorConsolidacionDTOJson()

        return map_consolidacion.dto_a_externo(sr.obtener_consolidacion_por_id(id))
    else:
        return [{"message": "GET!"}]


@bp.route("/consolidacion-query", methods=("GET",))
@bp.route("/consolidacion-query/<id>", methods=("GET",))
def dar_consolidacion_usando_query(id=None, region: str = ""):
    if id:
        region = request.args.get("region")
        query_resultado = ejecutar_query(ObtenerConsolidacion(id))
        map_consolidacion = MapeadorConsolidacionDTOJson()
        return map_consolidacion.dto_a_externo(query_resultado.resultado, region)
    else:
        return [{"message": "GET!"}]


async def ejecutar_comando_async(comando):
    ejecutar_commando(comando)
