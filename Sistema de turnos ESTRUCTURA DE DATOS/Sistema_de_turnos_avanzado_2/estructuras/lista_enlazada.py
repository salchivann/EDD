class _Nodo:
    __slots__ = ("dato", "anterior", "siguiente")

    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaEnlazadaDoble:

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
        resultado = []
        actual = self._cabeza
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def recorrer_inverso(self):
        resultado = []
        actual = self._cola
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.anterior
        return resultado
