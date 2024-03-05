import auditoria.seedwork.presentacion.api as api
import json, time
import asyncio

from auditoria.seedwork.dominio.excepciones import ExcepcionDominio
from flask import redirect, render_template, request, session, url_for
from flask import Response

from auditoria.modulos.auditoria.aplicacion.servicios import ServicioAuditoria
from auditoria.modulos.auditoria.aplicacion.mapeadores import MapeadorAuditoriaDTOJson
from auditoria.modulos.auditoria.aplicacion.comandos.auditar_compania import (
    AuditarCompania,
)
from auditoria.modulos.auditoria.aplicacion.queries.obtener_auditoria import (
    ObtenerAuditoria,
)

from auditoria.seedwork.aplicacion.comandos import ejecutar_commando
from auditoria.seedwork.aplicacion.comandos import despachar_commando
from auditoria.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint("auditoria", "/auditoria")


@bp.route("/auditoria", methods=("POST",))
def crear():
    try:
        crear_dict = request.json

        map_auditoria = MapeadorAuditoriaDTOJson()
        auditoria_dto = map_auditoria.externo_a_dto(crear_dict)

        sr = ServicioAuditoria()
        dto_final = sr.auditar_compania(auditoria_dto)

        return map_auditoria.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(
            json.dumps(dict(error=str(e))), status=400, mimetype="application/json"
        )


@bp.route("/auditoria-comando", methods=("POST",))
def crear_asincrona():
    try:
        session.clear()
        print("LLEGO AQUI")

        crear_dict = request.json

        map_auditoria = MapeadorAuditoriaDTOJson()
        auditoria_dto = map_auditoria.externo_a_dto(crear_dict)

        comando = AuditarCompania(
            auditoria_dto.fecha_creacion,
            auditoria_dto.fecha_actualizacion,
            auditoria_dto.id,
            auditoria_dto.compania,
            auditoria_dto.fecha,
            auditoria_dto.descripcion,
        )

        print("LLEGO AQUI 2")
        print(comando)

        ##despachar_commando(comando)
        ejecutar_commando(comando)

        return Response("{}", status=202, mimetype="application/json")
    except ExcepcionDominio as e:
        return Response(
            json.dumps(dict(error=str(e))), status=400, mimetype="application/json"
        )


@bp.route("/auditoria", methods=("GET",))
@bp.route("/auditoria/<id>", methods=("GET",))
def dar_auditoria(id=None):
    if id:
        sr = ServicioAuditoria()
        map_auditoria = MapeadorAuditoriaDTOJson()

        return map_auditoria.dto_a_externo(sr.obtener_auditoria_por_id(id))
    else:
        return [{"message": "GET!"}]


@bp.route("/auditoria-query", methods=("GET",))
@bp.route("/auditoria-query/<id>", methods=("GET",))
def dar_auditoria_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerAuditoria(id))
        map_auditoria = MapeadorAuditoriaDTOJson()

        return map_auditoria.dto_a_externo(query_resultado.resultado)
    else:
        return [{"message": "GET!"}]
