from __future__ import annotations
from dataclasses import dataclass, field
from auditoria.seedwork.dominio.eventos import EventoDominio
from datetime import datetime


@dataclass
class CompaniaAuditada(EventoDominio):
    id_auditoria: uuid.UUID = None
    id_compania: uuid.UUID = None
    fecha: str = None
    descripcion: str = None
