class _NodoPrioridad:
    __slots__ = ("dato", "prioridad", "siguiente")

    def __init__(self, dato, prioridad):
        self.dato = dato
        self.prioridad = prioridad
        self.siguiente = None


class ColaPrioridad:
    """
    TAD Cola de Prioridad implementada como una lista enlazada
    ORDENADA por prioridad (mayor prioridad al frente). Es una
    estructura distinta de la Cola normal: no respeta estrictamente
    el orden de llegada, sino el nivel de prioridad de cada elemento.

    Se usa en el sistema para la atención preferencial.

    Complejidad:
        insertar()               -> O(n) en el peor caso (se recorre
                                     la lista para ubicar la posición
                                     ordenada correcta)
        extraer_mayor_prioridad()-> O(1) (siempre se retira el frente)
        ver_frente()              -> O(1)
        recorrer()                -> O(n)
    """

    def __init__(self):
        self._frente = None
        self._tamano = 0

    def insertar(self, dato, prioridad):
        nuevo = _NodoPrioridad(dato, prioridad)
        if self._frente is None or prioridad > self._frente.prioridad:
            nuevo.siguiente = self._frente
            self._frente = nuevo
        else:
            actual = self._frente
            while actual.siguiente is not None and actual.siguiente.prioridad >= prioridad:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        self._tamano += 1

    def extraer_mayor_prioridad(self):
        if self.esta_vacia():
            return None
        nodo = self._frente
        self._frente = nodo.siguiente
        self._tamano -= 1
        return nodo.dato

    def ver_frente(self):
        return self._frente.dato if self._frente else None

    def esta_vacia(self):
        return self._frente is None

    def tamano(self):
        return self._tamano

    def recorrer(self):
        resultado = []
        actual = self._frente
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def eliminar(self, condicion):
        anterior = None
        actual = self._frente
        while actual is not None:
            if condicion(actual.dato):
                if anterior is None:
                    self._frente = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self._tamano -= 1
                return actual.dato
            anterior = actual
            actual = actual.siguiente
        return None
