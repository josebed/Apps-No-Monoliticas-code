import propdalpescoleccioncomp.seedwork.presentacion.api as api
import json

from propdalpescoleccioncomp.seedwork.dominio.excepciones import ExcepcionDominio
from flask import redirect, render_template, request, session, url_for
from flask import Response

from propdalpescoleccioncomp.modulos.companias.aplicacion.servicios import ServicioCompania
from propdalpescoleccioncomp.modulos.companias.aplicacion.mapeadores import MapeadorCompaniaDTOJson

from propdalpescoleccioncomp.seedwork.aplicacion.comandos import ejecutar_commando
from propdalpescoleccioncomp.seedwork.aplicacion.queries import ejecutar_query

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

    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route('/compania', methods=('GET',))
@bp.route('/compania/<id>', methods=('GET',))
def dar_compania(id=None):
    if id:
        sr = ServicioCompania()
        map_reserva = MapeadorCompaniaDTOJson()
        
        return map_reserva.dto_a_externo(sr.obtener_compania_por_id(id))
    else:
        return [{'message': 'GET!'}]
    
@bp.route('/compania-query', methods=('GET',))
@bp.route('/compania-query/<id>', methods=('GET',))
def dar_compania_usando_query(id=None):
    if id:
        crear_dict = ""
    else:
        return [{'message': 'GET!'}]