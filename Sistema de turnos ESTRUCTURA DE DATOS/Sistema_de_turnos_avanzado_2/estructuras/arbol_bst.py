# Clase que representa un nodo del árbol.
# Cada nodo almacena un dato y referencias
# hacia sus hijos izquierdo y derecho.
class _NodoArbol:
    __slots__ = ("dato", "izquierdo", "derecho")

    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


# TAD Árbol Binario de Búsqueda (BST).
# Contiene todas las operaciones para
# insertar, buscar y recorrer el árbol.
class ArbolBST:
    def __init__(self):
        self._raiz = None
        self._tamano = 0
    # Inserta un nuevo elemento en el árbol
    # utilizando un método recursivo.
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


    # Busca un elemento por su código
    # recorriendo el árbol de forma recursiva.
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


    # Realiza un recorrido Inorden, devolviendo
    # los elementos ordenados de menor a mayor.
    def recorrido_inorden(self):
        resultado = []
        self._inorden_rec(self._raiz, resultado)
        return resultado

    def _inorden_rec(self, nodo, resultado):
        if nodo is not None:
            self._inorden_rec(nodo.izquierdo, resultado)
            resultado.append(nodo.dato)
            self._inorden_rec(nodo.derecho, resultado)


    # Devuelve tamaño del arbol
    def tamano(self):
        return self._tamano
    
    # Calcula la altura del árbol (niveles)
    def altura(self):
        return self._altura_rec(self._raiz)

    def _altura_rec(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura_rec(nodo.izquierdo), self._altura_rec(nodo.derecho))


    # Organiza los nodos por niveles.
    # Se utiliza para representar gráficamente la estructura del árbol.
    def estructura_por_niveles(self):

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


    # Calcula la posición de cada nodo
    # para poder dibujar el árbol en pantalla.
    def obtener_disposicion(self):

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