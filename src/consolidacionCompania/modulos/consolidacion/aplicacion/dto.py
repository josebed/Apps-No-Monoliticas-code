from dataclasses import dataclass, field
from consolidacionCompania.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class ConsolidacionDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    numero: str = field(default_factory=str)
    tipo: str = field(default_factory=str)
