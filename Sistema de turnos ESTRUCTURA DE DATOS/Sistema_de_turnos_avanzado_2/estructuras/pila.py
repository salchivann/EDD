#Cada nodo almacena un dato y la referencia al siguiente.

class _NodoPila:
    __slots__ = ("dato", "siguiente")

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# TAD Pila (LIFO). El último elemento que entra es el primero en salir.
class Pila:

    def __init__(self):
        self._tope = None
        self._tamano = 0

    # Agrega un nuevo elemento en la parte superior de la pila.
    def apilar(self, dato):
        nuevo = _NodoPila(dato)
        nuevo.siguiente = self._tope
        self._tope = nuevo
        self._tamano += 1

    # Elimina y devuelve el elemento que se encuentra en el tope de la pila.
    def desapilar(self):
        if self.esta_vacia():
            return None
        nodo = self._tope
        self._tope = nodo.siguiente
        self._tamano -= 1
        return nodo.dato

    # Devuelve el elemento ubicado en el tope sin eliminarlo.
    def ver_tope(self):
        return self._tope.dato if self._tope else None

    # Verifica si la pila está vacía.
    def esta_vacia(self):
        return self._tope is None

    # Devuelve la cantidad de elementos almacenados.
    def tamano(self):
        return self._tamano

    # Recorre la pila desde el tope hasta el último elemento.
    def recorrer(self):
        resultado = []
        actual = self._tope
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado