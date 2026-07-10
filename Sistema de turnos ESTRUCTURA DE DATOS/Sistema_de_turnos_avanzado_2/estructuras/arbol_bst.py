class _NodoArbol:
    __slots__ = ("dato", "izquierdo", "derecho")

    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


class ArbolBST:
    """
    TAD Árbol Binario de Búsqueda (BST), indexado por el código del
    turno (cadena de texto). Se usa para consultar rápidamente el
    historial de turnos ya atendidos o cancelados por su
    identificador.

    Complejidad:
        insertar()  -> O(log n) promedio, O(n) en el peor caso
                       (árbol degenerado, p. ej. códigos ya ordenados)
        buscar()    -> O(log n) promedio, O(n) en el peor caso
        recorrido_inorden() -> O(n), produce los turnos ordenados
                                alfabéticamente por código
    """

    def __init__(self):
        self._raiz = None
        self._tamano = 0

    def insertar(self, dato):
        self._raiz = self._insertar_rec(self._raiz, dato)
        self._tamano += 1

    def _insertar_rec(self, nodo, dato):
        if nodo is None:
            return _NodoArbol(dato)
        if dato.codigo < nodo.dato.codigo:
            nodo.izquierdo = self._insertar_rec(nodo.izquierdo, dato)
        else:
            nodo.derecho = self._insertar_rec(nodo.derecho, dato)
        return nodo

    def buscar(self, codigo):
        return self._buscar_rec(self._raiz, codigo)

    def _buscar_rec(self, nodo, codigo):
        if nodo is None:
            return None
        if codigo == nodo.dato.codigo:
            return nodo.dato
        if codigo < nodo.dato.codigo:
            return self._buscar_rec(nodo.izquierdo, codigo)
        return self._buscar_rec(nodo.derecho, codigo)

    def recorrido_inorden(self):
        resultado = []
        self._inorden_rec(self._raiz, resultado)
        return resultado

    def _inorden_rec(self, nodo, resultado):
        if nodo is not None:
            self._inorden_rec(nodo.izquierdo, resultado)
            resultado.append(nodo.dato)
            self._inorden_rec(nodo.derecho, resultado)

    def tamano(self):
        return self._tamano

    def altura(self):
        return self._altura_rec(self._raiz)

    def _altura_rec(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura_rec(nodo.izquierdo), self._altura_rec(nodo.derecho))

    def estructura_por_niveles(self):
        """
        Devuelve una lista de niveles (BFS), cada uno con los nodos
        (o None si no existen) de ese nivel. Se conserva por
        compatibilidad, pero para dibujar el árbol se recomienda usar
        obtener_disposicion(), que produce una distribución compacta.
        """
        if self._raiz is None:
            return []
        niveles = []
        nivel_actual = [self._raiz]
        while any(n is not None for n in nivel_actual):
            niveles.append(nivel_actual)
            siguiente_nivel = []
            for nodo in nivel_actual:
                if nodo is not None:
                    siguiente_nivel.append(nodo.izquierdo)
                    siguiente_nivel.append(nodo.derecho)
                else:
                    siguiente_nivel.append(None)
                    siguiente_nivel.append(None)
            nivel_actual = siguiente_nivel
        return niveles

    def obtener_disposicion(self):
        """
        Calcula una posición compacta para cada nodo, pensada para
        dibujar el árbol sin dejar huecos vacíos entre nodos:

        - La coordenada X se asigna según el orden de un recorrido
          inorden (0, 1, 2, ...), de modo que los nodos quedan uno al
          lado del otro sin reservar espacio para ramas inexistentes.
        - La coordenada "profundidad" (Y) es el nivel del nodo dentro
          del árbol (raíz = 0).

        Devuelve una lista de tuplas:
            (turno, x, profundidad, codigo_del_padre)
        """
        resultado = []
        contador = [0]

        def rec(nodo, profundidad, codigo_padre):
            if nodo is None:
                return
            rec(nodo.izquierdo, profundidad + 1, nodo.dato.codigo)
            x = contador[0]
            contador[0] += 1
            resultado.append((nodo.dato, x, profundidad, codigo_padre))
            rec(nodo.derecho, profundidad + 1, nodo.dato.codigo)

        rec(self._raiz, 0, None)
        return resultado
