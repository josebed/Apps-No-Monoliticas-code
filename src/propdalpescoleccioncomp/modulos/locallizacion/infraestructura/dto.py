from propdalpescoleccioncomp.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Localizacion(db.Model):
    __tablename__ = "localizaciones"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    ubicacion = db.Column(db.String, nullable=False)
    ciudad = db.Column(db.String, nullable=False)
    numero = db.Column(db.String, nullable=False)
    latitud = db.Column(db.String, nullable=False)
    longitud = db.Column(db.String, nullable=False)