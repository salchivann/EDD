from turno import Turno
from estructuras.pila import Pila
from estructuras.cola import Cola
from estructuras.cola_prioridad import ColaPrioridad
from estructuras.lista_enlazada import ListaEnlazadaDoble
from estructuras.arbol_bst import ArbolBST


class GestorTurnos:
    def __init__(self):
        self.cola_normal = Cola()
        self.cola_prioridad = ColaPrioridad()
        self.pila_historial = Pila()
        self.registro = ListaEnlazadaDoble()
        self.arbol_historial = ArbolBST()
        self._contador_normal = 0
        self._contador_prioritario = 0

    # ---------------- Generar turnos ----------------
    def agregar_turno(self, tipo):
        if tipo == "Prioritario":
            self._contador_prioritario += 1
            codigo = f"P-{self._contador_prioritario}"
            turno = Turno(codigo, tipo, prioridad=1)
            self.cola_prioridad.insertar(turno, prioridad=1)
        else:
            self._contador_normal += 1
            codigo = f"N-{self._contador_normal}"
            turno = Turno(codigo, tipo, prioridad=0)
            self.cola_normal.encolar(turno)

        self.registro.insertar_final(turno)
        return turno

    # ---------------- Atender turnos ----------------
    def atender_turno_normal(self):
        turno = self.cola_normal.desencolar()
        if turno is not None:
            self._finalizar_turno(turno, atendido=True)
        return turno

    def atender_turno_prioritario(self):
        turno = self.cola_prioridad.extraer_mayor_prioridad()
        if turno is not None:
            self._finalizar_turno(turno, atendido=True)
        return turno

    def _finalizar_turno(self, turno, atendido):
        if atendido:
            turno.marcar_atendido()
        else:
            turno.marcar_cancelado()
        self.pila_historial.apilar(turno)
        self.arbol_historial.insertar(turno)

    # ---------------- Cancelar ----------------
    def cancelar_turno(self, codigo):
        turno = self.cola_normal.eliminar(lambda t: t.codigo == codigo)
        if turno is None:
            turno = self.cola_prioridad.eliminar(lambda t: t.codigo == codigo)
        if turno is not None:
            self._finalizar_turno(turno, atendido=False)
        return turno

    # ---------------- Consultas ----------------
    def consultar_cola_normal(self):
        return self.cola_normal.recorrer()

    def consultar_cola_prioridad(self):
        return self.cola_prioridad.recorrer()

    def consultar_historial(self):
        """Del más reciente al más antiguo (comportamiento LIFO de la pila)."""
        return self.pila_historial.recorrer()

    def buscar_en_historial(self, codigo):
        """Búsqueda eficiente en el árbol binario de búsqueda."""
        return self.arbol_historial.buscar(codigo)

    def historial_ordenado_por_codigo(self):
        return self.arbol_historial.recorrido_inorden()

    def exportar_historial(self, ruta="historial.txt"):
        turnos = self.consultar_historial()
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("===== HISTORIAL DE TURNOS =====\n")
            if not turnos:
                f.write("No existen turnos en el historial.\n")
            for t in turnos:
                f.write(t.mostrar_datos() + "\n")
        return ruta

    def metricas(self):
        return {
            "en_cola_normal": self.cola_normal.tamano(),
            "en_cola_prioridad": self.cola_prioridad.tamano(),
            "atendidos_o_cancelados": self.pila_historial.tamano(),
            "total_generados": self.registro.tamano(),
            "altura_arbol_historial": self.arbol_historial.altura(),
        }

    def mostrar_turnos(self):
        """Se conserva por compatibilidad: imprime cola normal y prioritaria."""
        print("\n===== COLA NORMAL =====")
        if self.cola_normal.esta_vacia():
            print("Vacía.")
        for t in self.consultar_cola_normal():
            print(t.mostrar_datos())

        print("\n===== COLA PRIORITARIA =====")
        if self.cola_prioridad.esta_vacia():
            print("Vacía.")
        for t in self.consultar_cola_prioridad():
            print(t.mostrar_datos())
