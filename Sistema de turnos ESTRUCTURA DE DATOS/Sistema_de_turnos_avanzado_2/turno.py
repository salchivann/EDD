from datetime import datetime


class Turno:
    """
    TAD (Tipo Abstracto de Datos) Turno.

    Representa un ticket de atención dentro del sistema. Encapsula los
    datos esenciales (código, tipo, estado, tiempos) y expone únicamente
    operaciones controladas sobre ese estado (marcar_atendido,
    marcar_cancelado), ocultando al resto del sistema los detalles de
    su representación interna. Esto es lo que lo convierte en un TAD y
    no en una simple estructura de datos "plana".
    """

    ESTADOS_VALIDOS = ("En espera", "Atendido", "Cancelado")

    def __init__(self, codigo, tipo, prioridad=0):
        self.codigo = codigo
        self.tipo = tipo                 # "Normal" o "Prioritario"
        self.prioridad = prioridad       # 0 = normal, 1 = prioritario
        self.estado = "En espera"
        self.hora_generado = datetime.now().strftime("%H:%M:%S")
        self.hora_atendido = None

    def marcar_atendido(self):
        self.estado = "Atendido"
        self.hora_atendido = datetime.now().strftime("%H:%M:%S")

    def marcar_cancelado(self):
        self.estado = "Cancelado"
        self.hora_atendido = datetime.now().strftime("%H:%M:%S")

    def mostrar_datos(self):
        base = f"Turno: {self.codigo} | Tipo: {self.tipo} | Estado: {self.estado} | Generado: {self.hora_generado}"
        if self.hora_atendido:
            base += f" | Finalizado: {self.hora_atendido}"
        return base

    def __str__(self):
        return self.mostrar_datos()

    def __repr__(self):
        return f"Turno({self.codigo!r}, {self.tipo!r}, estado={self.estado!r})"
