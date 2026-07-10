class _NodoCola:
    __slots__ = ("dato", "siguiente")

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Cola:
    """
    TAD Cola (Queue) implementada con nodos enlazados y punteros de
    frente y final, lo que permite encolar y desencolar en O(1).

    Comportamiento FIFO: el primero en entrar es el primero en salir.
    Se usa en el sistema para la atención en orden de llegada
    (turnos normales).

    Complejidad:
        encolar()     -> O(1)
        desencolar()  -> O(1)
        ver_frente()  -> O(1)
        eliminar()    -> O(n)  (se debe recorrer para ubicar el elemento)
        recorrer()    -> O(n)
    """

    def __init__(self):
        self._frente = None
        self._final = None
        self._tamano = 0

    def encolar(self, dato):
        nuevo = _NodoCola(dato)
        if self._final is None:
            self._frente = nuevo
            self._final = nuevo
        else:
            self._final.siguiente = nuevo
            self._final = nuevo
        self._tamano += 1

    def desencolar(self):
        if self.esta_vacia():
            return None
        nodo = self._frente
        self._frente = nodo.siguiente
        if self._frente is None:
            self._final = None
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
        """
        Elimina y devuelve el primer elemento para el que
        condicion(dato) sea verdadero. Se usa para cancelar un turno
        que aún está en espera. O(n).
        """
        anterior = None
        actual = self._frente
        while actual is not None:
            if condicion(actual.dato):
                if anterior is None:
                    self._frente = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                if actual is self._final:
                    self._final = anterior
                self._tamano -= 1
                return actual.dato
            anterior = actual
            actual = actual.siguiente
        return None
