class _Nodo:
    __slots__ = ("dato", "anterior", "siguiente")

    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None


class ListaEnlazadaDoble:
    """
    TAD Lista Enlazada Doble.

    Mantiene el registro dinámico de TODOS los turnos generados en el
    sistema (sin importar si ya fueron atendidos, cancelados o siguen
    en espera), permitiendo insertar, eliminar y recorrer en ambos
    sentidos. Se usa como el "maestro" de turnos, independiente de en
    qué cola o pila se encuentre cada uno en un momento dado.

    Complejidad:
        insertar_final()      -> O(1) (se mantiene puntero a la cola)
        buscar_por_codigo()   -> O(n)
        eliminar_por_codigo() -> O(n)
        recorrer()            -> O(n)
    """

    def __init__(self):
        self._cabeza = None
        self._cola = None
        self._tamano = 0

    def insertar_final(self, dato):
        nuevo = _Nodo(dato)
        if self._cabeza is None:
            self._cabeza = nuevo
            self._cola = nuevo
        else:
            nuevo.anterior = self._cola
            self._cola.siguiente = nuevo
            self._cola = nuevo
        self._tamano += 1

    def buscar_por_codigo(self, codigo):
        actual = self._cabeza
        while actual is not None:
            if actual.dato.codigo == codigo:
                return actual.dato
            actual = actual.siguiente
        return None

    def eliminar_por_codigo(self, codigo):
        actual = self._cabeza
        while actual is not None:
            if actual.dato.codigo == codigo:
                if actual.anterior is not None:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self._cabeza = actual.siguiente
                if actual.siguiente is not None:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self._cola = actual.anterior
                self._tamano -= 1
                return actual.dato
            actual = actual.siguiente
        return None

    def tamano(self):
        return self._tamano

    def recorrer(self):
        """Recorrido de cabeza a cola. O(n)."""
        resultado = []
        actual = self._cabeza
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def recorrer_inverso(self):
        """Recorrido de cola a cabeza (ventaja frente a la lista simple). O(n)."""
        resultado = []
        actual = self._cola
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.anterior
        return resultado
