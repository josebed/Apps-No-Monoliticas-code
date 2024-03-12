from functools import singledispatch
from abc import ABC, abstractmethod
from auditoriaCompania.seedwork.dominio.eventos import EventoDominio

class EventoHandler(ABC):
    @abstractmethod
    def handle(self, evento: EventoDominio):
        raise NotImplementedError()

@singledispatch
def oir_evento(evento):
    raise NotImplementedError(f'No existe implementación para el evento de tipo {type(evento).__name__}')