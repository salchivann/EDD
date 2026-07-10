# Sistema de Gestión de Atención al Cliente y Turnos Inteligentes

## Instalación
pip install -r requirements.txt

## Ejecución
python main.py

## Estructura del proyecto
- turno.py                     -> TAD Turno
- gestorTurnos.py               -> Orquestador de todas las estructuras
- interfaz.py                   -> Interfaz gráfica (customtkinter)
- main.py                       -> Punto de entrada
- estructuras/
  - pila.py                     -> TAD Pila (historial)
  - cola.py                     -> TAD Cola (atención normal)
  - cola_prioridad.py           -> TAD Cola de Prioridad (atención preferencial)
  - lista_enlazada.py           -> TAD Lista Enlazada Doble (registro maestro)
  - arbol_bst.py                -> TAD Árbol Binario de Búsqueda (historial indexado)
