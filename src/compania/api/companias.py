import compania.seedwork.presentacion.api as api
import json, time
import asyncio

from compania.seedwork.dominio.excepciones import ExcepcionDominio
from flask import redirect, render_template, request, session, url_for
from flask import Response

from compania.modulos.companias.aplicacion.servicios import ServicioCompania
from compania.modulos.companias.aplicacion.mapeadores import MapeadorCompaniaDTOJson
from compania.modulos.companias.aplicacion.comandos.crear_compania import CrearCompania
from compania.modulos.companias.aplicacion.queries.obtener_compania import ObtenerCompania

from compania.seedwork.aplicacion.comandos import ejecutar_commando
from compania.seedwork.aplicacion.comandos import despachar_commando
from compania.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('companias', '/companias')

@bp.route('/compania', methods=('POST',))
def crear():
    try:
        crear_dict = request.json

        map_compania = MapeadorCompaniaDTOJson()
        compania_dto = map_compania.externo_a_dto(crear_dict)
        
        sr = ServicioCompania()
        dto_final = sr.crear_compania(compania_dto)

        return map_compania.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route('/compania-comando', methods=('POST',))
def crear_asincrona():
    try:
        crear_dict = request.json

        map_compania = MapeadorCompaniaDTOJson()
        compania_dto = map_compania.externo_a_dto(crear_dict)

        comando = CrearCompania(compania_dto.fecha_creacion, compania_dto.fecha_actualizacion, compania_dto.id, 
                                compania_dto.nombre, compania_dto.numero, compania_dto.tipo)

        despachar_commando(comando)
 
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route('/compania', methods=('GET',))
@bp.route('/compania/<id>', methods=('GET',))
def dar_compania(id=None):
    if id:
        sr = ServicioCompania()
        map_compania = MapeadorCompaniaDTOJson()
        
        return map_compania.dto_a_externo(sr.obtener_compania_por_id(id))
    else:
        return [{'message': 'GET!'}]
    
@bp.route('/compania-query', methods=('GET',))
@bp.route('/compania-query/<id>', methods=('GET',))
def dar_compania_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerCompania(id))
        map_compania = MapeadorCompaniaDTOJson()
        
        return map_compania.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]

@bp.route('/compania-comando2', methods=('POST',))
def ejecutar_comando_async():
    try:
        crear_dict = request.json

        map_compania = MapeadorCompaniaDTOJson()
        compania_dto = map_compania.externo_a_dto(crear_dict)

        comando = CrearCompania(compania_dto.fecha_creacion, compania_dto.fecha_actualizacion, compania_dto.id, 
                                compania_dto.nombre, compania_dto.numero, compania_dto.tipo)

        ejecutar_commando(comando)

        return Response('{}', status=200, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json') 