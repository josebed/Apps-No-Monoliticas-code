from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from auditoriaCompania.seedwork.dominio.eventos import EventoDominio
from datetime import datetime


class EventoCompania(EventoDominio): ...


@dataclass
class CompaniaAuditada(EventoAuditoria):
    id_compania: uuid.UUID = None
    id_auditoria: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None


@dataclass
class AuditoriaRevertida(EventoAuditoria):
    id_compania: uuid.UUID = None
    id_correlacion: str = None
    descripcion: str = None
    fecha_actualizacion: datetime = None


@dataclass
class AuditoriaFallida(EventoAuditoria):
    id_reid_companiaserva: uuid.UUID = None
    id_correlacion: str = None
    descripcion: str = None
    fecha_actualizacion: datetime = None
