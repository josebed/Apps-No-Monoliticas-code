from auditoriaCompania.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from auditoriaCompania.seedwork.aplicacion.comandos import Comando
from auditoriaCompania.seedwork.dominio.eventos import EventoDominio

from auditoriaCompania.modulos.sagas.aplicacion.comandos.compania import AuditarCompania, RevertirAuditoria
from auditoriaCompania.modulos.sagas.dominio.eventos.compania import CompaniaAuditada, AuditoriaRevertida, AuditoriaFallida


class CoordinadorAuditoria(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=AuditarCompania, evento=CompaniaAuditada, error=AuditoriaFallida, compensacion=AuditoriaRevertida)
            Fin(index=5)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar():
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        ...


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorAuditoria()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")