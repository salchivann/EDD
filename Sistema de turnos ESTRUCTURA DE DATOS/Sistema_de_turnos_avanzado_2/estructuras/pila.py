class _NodoPila:
    __slots__ = ("dato", "siguiente")

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    """
    TAD Pila (Stack) implementada con nodos enlazados (sin usar listas
    de Python como estructura de almacenamiento).

    Comportamiento LIFO: el último elemento apilado es el primero en
    salir. Se usa en el sistema para el historial de turnos atendidos
    o cancelados, de modo que lo más reciente aparece primero.

    Complejidad:
        apilar()      -> O(1)
        desapilar()   -> O(1)
        ver_tope()    -> O(1)
        recorrer()    -> O(n)
    """

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
        """Devuelve los elementos del tope hacia la base. O(n)."""
        resultado = []
        actual = self._tope
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado
