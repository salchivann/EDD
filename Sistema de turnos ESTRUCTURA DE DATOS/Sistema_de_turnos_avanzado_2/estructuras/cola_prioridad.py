# Almacena el dato, su prioridad
# y la referencia al siguiente nodo.
class _NodoPrioridad:
    __slots__ = ("dato", "prioridad", "siguiente")

    def __init__(self, dato, prioridad):
        self.dato = dato
        self.prioridad = prioridad
        self.siguiente = None

# Mantiene los elementos ordenados según su nivel de prioridad.
class ColaPrioridad:

    def __init__(self):
        self._frente = None
        self._tamano = 0

# Inserta un elemento en la posición que le corresponde según su prioridad. A mayor prioridad, más cerca del frente.
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

    # Extrae y devuelve el elemento con la mayor prioridad, que siempre se encuentra al frente.
    def extraer_mayor_prioridad(self):
        if self.esta_vacia():
            return None
        nodo = self._frente
        self._frente = nodo.siguiente
        self._tamano -= 1
        return nodo.dato

    # Devuelve el elemento que está al frente sin eliminarlo.
    def ver_frente(self):
        return self._frente.dato if self._frente else None


    # Verifica si la cola se encuentra vacía.
    def esta_vacia(self):
        return self._frente is None


    # Devuelve la cantidad de elementos almacenados.
    def tamano(self):
        return self._tamano


    # Recorre toda la cola y devuelve una lista con los elementos en orden de prioridad.
    def recorrer(self):
        resultado = []
        actual = self._frente
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado


    # Elimina un elemento que cumpla una condición específica y lo devuelve.
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