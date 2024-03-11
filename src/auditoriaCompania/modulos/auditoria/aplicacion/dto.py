from dataclasses import dataclass, field
from auditoria.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class AuditoriaDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    compania: str = field(default_factory=str)
    fecha: str = field(default_factory=str)
    descripcion: str = field(default_factory=str)