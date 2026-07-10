from datetime import datetime

class Turno:
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
