class _NodoPila:
    __slots__ = ("dato", "siguiente")

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:

    def __init__(self):
        self._tope = None
        self._tamano = 0

    def apilar(self, dato):
        nuevo = _NodoPila(dato)
        nuevo.siguiente = self._tope
        self._tope = nuevo
        self._tamano += 1

    def desapilar(self):
        if self.esta_vacia():
            return None
        nodo = self._tope
        self._tope = nodo.siguiente
        self._tamano -= 1
        return nodo.dato

    def ver_tope(self):
        return self._tope.dato if self._tope else None

    def esta_vacia(self):
        return self._tope is None

    def tamano(self):
        return self._tamano

    def recorrer(self):
        resultado = []
        actual = self._tope
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado
