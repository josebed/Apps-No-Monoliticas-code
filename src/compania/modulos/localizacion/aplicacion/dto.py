from dataclasses import dataclass, field
from propdalpescoleccioncomp.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class LocalizacionDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    ubicacion: str = field(default_factory=str)
    ciudad: str = field(default_factory=str)
    numero: str = field(default_factory=str)
    latitud: str = field(default_factory=str)
    longitud: str = field(default_factory=str)