from auditoriaCompania.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from auditoriaCompania.seedwork.aplicacion.comandos import Comando
from auditoriaCompania.seedwork.dominio.eventos import EventoDominio

from auditoriaCompania.modulos.sagas.aplicacion.comandos.compania import AuditarCompania, RevertirAuditoria, CrearCompania, HabilitarVisualizacionCompania
from auditoriaCompania.modulos.sagas.dominio.eventos.compania import CompaniaAuditada, AuditoriaRevertida, AuditoriaFallida, CompaniaCreada
from auditoriaCompania.seedwork.aplicacion.eventos import oir_evento as oir


class CoordinadorAuditoria(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearCompania, evento=CompaniaCreada, error=AuditoriaFallida, compensacion=AuditoriaRevertida, exitosa=False),
            Transaccion(index=2, comando=AuditarCompania, evento=CompaniaAuditada, error=AuditoriaFallida, compensacion=AuditoriaRevertida, exitosa=False),
            Transaccion(index=3, comando=HabilitarVisualizacionCompania, evento=CompaniaAuditada, error=AuditoriaFallida, compensacion=AuditoriaRevertida, exitosa=False),
            Fin(index=4)
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
        print(tipo_comando.__name__)
        print(evento)


        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        ...


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
@oir.register(EventoDominio)
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorAuditoria()
        coordinador.inicializar_pasos()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")