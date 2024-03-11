from auditoriaCompania.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()


class Auditoria(db.Model):
    __tablename__ = "auditoria"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    compania = db.Column(db.String, nullable=False)
    fecha = db.Column(db.String, nullable=False)
    descripcion = db.Column(db.String, nullable=False)
