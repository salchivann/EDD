# Clase que representa un nodo la lista doblemente enlazada. 
# Cada nodo almacena un dato y referencias al nodo anterior y siguiente.
class _Nodo:
    __slots__ = ("dato", "anterior", "siguiente")

    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

# TAD Lista Doblemente Enlazada. Permite recorrer los elementos tanto hacia adelante como hacia atrás.
class ListaEnlazadaDoble:

    def __init__(self):
        self._cabeza = None
        self._cola = None
        self._tamano = 0

    # Inserta un nuevo elemento al final de la lista.
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

    # Busca un elemento utilizando su código y lo devuelve si existe.
    def buscar_por_codigo(self, codigo):
        actual = self._cabeza
        while actual is not None:
            if actual.dato.codigo == codigo:
                return actual.dato
            actual = actual.siguiente
        return None

    # Elimina un elemento por su código y actualiza los enlaces de la lista.
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

    # Devuelve la cantidad de elementos de la lista.
    def tamano(self):
        return self._tamano

    # Recorre la lista desde la cabeza hasta la cola.
    def recorrer(self):
        resultado = []
        actual = self._cabeza
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    # Recorre la lista en sentido inverso, desde la cola hasta la cabeza.
    def recorrer_inverso(self):
        resultado = []
        actual = self._cola
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.anterior
        return resultado