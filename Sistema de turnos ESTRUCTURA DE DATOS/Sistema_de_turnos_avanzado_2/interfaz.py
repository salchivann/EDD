import os
import tkinter as tk
from tkinter import messagebox, filedialog
import customtkinter as ctk
from gestorTurnos import GestorTurnos

# =========================
# CONFIGURACIÓN
# =========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# =========================
# GESTOR
# =========================

gestor = GestorTurnos()

# =========================
# VENTANA
# =========================

ventana = ctk.CTk()
ventana.title("Sistema de Turnos")
ventana.geometry("1050x600")

# =========================
# FRAME LATERAL (MENÚ)
# =========================

frame_menu = ctk.CTkScrollableFrame(ventana, width=220, corner_radius=0)
frame_menu.pack(side="left", fill="y")

# =========================
# FRAME PRINCIPAL
# =========================

frame_principal = ctk.CTkFrame(ventana)
frame_principal.pack(side="right", expand=True, fill="both")


def limpiar_frame():
    for widget in frame_principal.winfo_children():
        widget.destroy()


def titulo_pantalla(texto):
    lbl = ctk.CTkLabel(frame_principal, text=texto, font=("Arial", 28, "bold"))
    lbl.pack(pady=20)
    return lbl


# =========================
# PANTALLA: INICIO
# =========================

def mostrar_inicio():
    limpiar_frame()
    titulo_pantalla("SISTEMA DE TURNOS")
    ctk.CTkLabel(
        frame_principal,
        text="Gestión de atención al cliente y turnos inteligentes",
        font=("Arial", 18),
    ).pack(pady=5)
    ctk.CTkLabel(
        frame_principal,
        text="Estructuras: Cola, Cola de prioridad, Pila, Lista enlazada doble y Árbol BST",
        font=("Arial", 14),
        text_color="gray",
    ).pack(pady=5)


# =========================
# PANTALLA: NUEVO TURNO
# =========================

def mostrar_nuevo_turno():
    limpiar_frame()
    titulo_pantalla("NUEVO TURNO")

    resultado = ctk.CTkLabel(frame_principal, text="Seleccione un tipo de turno", font=("Arial", 18))
    resultado.pack(pady=15)

    def turno_normal():
        t = gestor.agregar_turno("Normal")
        resultado.configure(text=f"Turno generado: {t.codigo}")

    def turno_prioritario():
        t = gestor.agregar_turno("Prioritario")
        resultado.configure(text=f"Turno generado: {t.codigo}")

    ctk.CTkButton(frame_principal, text="Turno Normal", command=turno_normal, width=250, height=50).pack(pady=10)
    ctk.CTkButton(frame_principal, text="Turno Prioritario", command=turno_prioritario, width=250, height=50).pack(pady=10)


# =========================
# PANTALLA: ATENDER TURNOS
# =========================

def mostrar_atender_turnos():
    limpiar_frame()
    titulo_pantalla("ATENDER TURNOS")

    resultado = ctk.CTkLabel(frame_principal, text="Use los botones para atender el siguiente turno", font=("Arial", 16))
    resultado.pack(pady=15)

    def atender_normal():
        t = gestor.atender_turno_normal()
        if t:
            resultado.configure(text=f"Atendido (cola normal): {t.mostrar_datos()}")
        else:
            resultado.configure(text="No hay turnos en la cola normal.")

    def atender_prioritario():
        t = gestor.atender_turno_prioritario()
        if t:
            resultado.configure(text=f"Atendido (prioritario): {t.mostrar_datos()}")
        else:
            resultado.configure(text="No hay turnos en la cola de prioridad.")

    ctk.CTkButton(frame_principal, text="Atender siguiente turno normal", command=atender_normal,
                  width=320, height=50).pack(pady=10)
    ctk.CTkButton(frame_principal, text="Atender siguiente turno prioritario", command=atender_prioritario,
                  width=320, height=50, fg_color="#8e44ad", hover_color="#5b2c6f").pack(pady=10)

    # Cancelar turno
    ctk.CTkLabel(frame_principal, text="Cancelar turno por código:", font=("Arial", 14)).pack(pady=(30, 5))
    entrada_cancelar = ctk.CTkEntry(frame_principal, placeholder_text="Ej: N-3", width=200)
    entrada_cancelar.pack(pady=5)

    def cancelar():
        codigo = entrada_cancelar.get().strip()
        t = gestor.cancelar_turno(codigo)
        if t:
            messagebox.showinfo("Turno cancelado", f"Se canceló: {t.mostrar_datos()}")
        else:
            messagebox.showwarning("No encontrado", f"No existe un turno en espera con código '{codigo}'.")

    ctk.CTkButton(frame_principal, text="Cancelar turno", command=cancelar,
                  fg_color="red", hover_color="darkred", width=200).pack(pady=10)


# =========================
# PANTALLA: VER COLAS ACTUALES
# =========================

def mostrar_colas():
    limpiar_frame()
    titulo_pantalla("COLAS ACTUALES")

    contenedor = ctk.CTkFrame(frame_principal, fg_color="transparent")
    contenedor.pack(expand=True, fill="both", padx=20, pady=10)

    col_normal = ctk.CTkFrame(contenedor)
    col_normal.pack(side="left", expand=True, fill="both", padx=10)
    ctk.CTkLabel(col_normal, text="Cola Normal (FIFO)", font=("Arial", 18, "bold")).pack(pady=10)

    turnos_normales = gestor.consultar_cola_normal()
    if not turnos_normales:
        ctk.CTkLabel(col_normal, text="Vacía.").pack(pady=10)
    for t in turnos_normales:
        ctk.CTkLabel(col_normal, text=t.mostrar_datos(), font=("Arial", 13)).pack(pady=3, anchor="w", padx=10)

    col_prioridad = ctk.CTkFrame(contenedor)
    col_prioridad.pack(side="left", expand=True, fill="both", padx=10)
    ctk.CTkLabel(col_prioridad, text="Cola de Prioridad", font=("Arial", 18, "bold")).pack(pady=10)

    turnos_prioridad = gestor.consultar_cola_prioridad()
    if not turnos_prioridad:
        ctk.CTkLabel(col_prioridad, text="Vacía.").pack(pady=10)
    for t in turnos_prioridad:
        ctk.CTkLabel(col_prioridad, text=t.mostrar_datos(), font=("Arial", 13)).pack(pady=3, anchor="w", padx=10)

    nota = ("Diferencia clave: la cola normal SIEMPRE respeta el orden de llegada. "
            "La cola de prioridad reordena internamente para que un turno prioritario "
            "sea atendido antes que uno normal, aunque haya llegado después.")
    ctk.CTkLabel(frame_principal, text=nota, font=("Arial", 12), text_color="gray",
                 wraplength=900, justify="left").pack(pady=15)

    ctk.CTkButton(frame_principal, text="Actualizar", command=mostrar_colas, width=150).pack(pady=5)


# =========================
# PANTALLA: HISTORIAL (PILA)
# =========================

def mostrar_historial():
    limpiar_frame()
    titulo_pantalla("HISTORIAL DE TURNOS (Pila)")
    ctk.CTkLabel(frame_principal, text="Orden: del más reciente al más antiguo",
                 font=("Arial", 13), text_color="gray").pack(pady=(0, 10))

    scroll = ctk.CTkScrollableFrame(frame_principal, width=850, height=350)
    scroll.pack(pady=10)

    turnos = gestor.consultar_historial()
    if not turnos:
        ctk.CTkLabel(scroll, text="No existen turnos en el historial.").pack(pady=10)
    for t in turnos:
        ctk.CTkLabel(scroll, text=t.mostrar_datos(), font=("Arial", 13)).pack(pady=3, anchor="w", padx=10)

    def exportar():
        ruta = filedialog.asksaveasfilename(
            title="Guardar historial",
            defaultextension=".txt",
            initialfile="historial_turnos.txt",
            filetypes=[("Archivo de texto", "*.txt")],
        )
        if not ruta:  # el usuario canceló el diálogo
            return
        ruta_final = gestor.exportar_historial(ruta)
        ruta_absoluta = os.path.abspath(ruta_final)
        if os.path.exists(ruta_absoluta):
            messagebox.showinfo("Exportado", f"Historial exportado correctamente en:\n{ruta_absoluta}")
        else:
            messagebox.showerror("Error", "No se pudo crear el archivo. Verifique los permisos de la carpeta.")

    ctk.CTkButton(frame_principal, text="Exportar historial (.txt)", command=exportar, width=220).pack(pady=10)


# =========================
# PANTALLA: BUSCAR EN HISTORIAL (BST)
# =========================

def mostrar_buscar():
    limpiar_frame()
    titulo_pantalla("BUSCAR TURNO EN HISTORIAL (Árbol BST)")

    entrada = ctk.CTkEntry(frame_principal, placeholder_text="Código, ej: N-1", width=250)
    entrada.pack(pady=10)

    resultado = ctk.CTkLabel(frame_principal, text="", font=("Arial", 15), wraplength=800)
    resultado.pack(pady=15)

    def buscar():
        codigo = entrada.get().strip()
        t = gestor.buscar_en_historial(codigo)
        if t:
            resultado.configure(text=f"Encontrado:\n{t.mostrar_datos()}")
        else:
            resultado.configure(text=f"No se encontró ningún turno con código '{codigo}' en el historial.")

    ctk.CTkButton(frame_principal, text="Buscar", command=buscar, width=150).pack(pady=5)

    ctk.CTkLabel(frame_principal, text="Historial ordenado por código (recorrido inorden del BST):",
                 font=("Arial", 14, "bold")).pack(pady=(25, 5))
    ctk.CTkLabel(frame_principal, text="Escriba un código arriba y presione \"Buscar\" para ver todos sus datos.",
                 font=("Arial", 11), text_color="gray").pack(pady=(0, 5))

    scroll = ctk.CTkScrollableFrame(frame_principal, width=850, height=200)
    scroll.pack(pady=5)
    ordenados = gestor.historial_ordenado_por_codigo()
    if not ordenados:
        ctk.CTkLabel(scroll, text="El historial está vacío.").pack(pady=10)
    else:
        columnas = 8
        for i, t in enumerate(ordenados):
            fila, col = divmod(i, columnas)
            ctk.CTkLabel(
                scroll, text=t.codigo, font=("Arial", 12, "bold"),
                fg_color="#2b2b2b", corner_radius=6, width=70, height=28,
            ).grid(row=fila, column=col, padx=6, pady=6)


# =========================
# PANTALLA: VISUALIZACIÓN GRÁFICA DEL ÁRBOL
# =========================

def mostrar_visualizacion_arbol():
    limpiar_frame()
    titulo_pantalla("VISUALIZACIÓN DEL ÁRBOL BST (Historial)")
    ctk.CTkLabel(frame_principal, text="Use las barras de desplazamiento si el árbol no cabe completo",
                 font=("Arial", 12), text_color="gray").pack(pady=(0, 5))

    disposicion = gestor.arbol_historial.obtener_disposicion()

    # Contenedor con canvas + scrollbars (horizontal y vertical)
    contenedor = tk.Frame(frame_principal, bg="#1a1a1a")
    contenedor.pack(pady=10, padx=10, expand=True, fill="both")

    v_scroll = tk.Scrollbar(contenedor, orient="vertical")
    h_scroll = tk.Scrollbar(contenedor, orient="horizontal")

    espacio_x = 65     # separación horizontal entre nodos vecinos (compacto)
    espacio_y = 75      # separación vertical entre niveles
    margen = 45
    radio = 20

    if not disposicion:
        ancho_total, alto_total = 700, 300
    else:
        max_x = max(d[1] for d in disposicion)
        max_prof = max(d[2] for d in disposicion)
        ancho_total = max(500, margen * 2 + max_x * espacio_x)
        alto_total = max(300, margen * 2 + max_prof * espacio_y)

    ancho_visible = min(ancho_total, 750)
    alto_visible = min(alto_total, 420)

    canvas = tk.Canvas(
        contenedor, bg="#1a1a1a", highlightthickness=0,
        width=ancho_visible, height=alto_visible,
        scrollregion=(0, 0, ancho_total, alto_total),
        yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set,
    )
    v_scroll.config(command=canvas.yview)
    h_scroll.config(command=canvas.xview)

    canvas.grid(row=0, column=0, sticky="nsew")
    v_scroll.grid(row=0, column=1, sticky="ns")
    h_scroll.grid(row=1, column=0, sticky="ew")
    contenedor.grid_rowconfigure(0, weight=1)
    contenedor.grid_columnconfigure(0, weight=1)

    if not disposicion:
        canvas.create_text(ancho_total / 2, alto_total / 2,
                            text="El árbol está vacío. Atienda o cancele algún turno primero.",
                            fill="white", font=("Arial", 14))
    else:
        # Posición en píxeles de cada nodo, indexado por código de turno
        posiciones = {}
        for turno, x, profundidad, _codigo_padre in disposicion:
            px = margen + x * espacio_x
            py = margen + profundidad * espacio_y
            posiciones[turno.codigo] = (px, py)

        # Primero las líneas (para que queden detrás de los círculos)
        for turno, x, profundidad, codigo_padre in disposicion:
            if codigo_padre is not None and codigo_padre in posiciones:
                px, py = posiciones[codigo_padre]
                x2, y2 = posiciones[turno.codigo]
                canvas.create_line(px, py, x2, y2, fill="#5599ff", width=2)

        # Luego los nodos
        for turno, x, profundidad, _codigo_padre in disposicion:
            cx, cy = posiciones[turno.codigo]
            canvas.create_oval(cx - radio, cy - radio, cx + radio, cy + radio,
                                fill="#2e86de", outline="white", width=2)
            canvas.create_text(cx, cy, text=turno.codigo, fill="white", font=("Arial", 9, "bold"))

    ctk.CTkButton(frame_principal, text="Actualizar", command=mostrar_visualizacion_arbol, width=150).pack(pady=10)


# =========================
# PANTALLA: DASHBOARD DE MÉTRICAS
# =========================

def mostrar_dashboard():
    limpiar_frame()
    titulo_pantalla("DASHBOARD DE MÉTRICAS")

    m = gestor.metricas()
    etiquetas = {
        "en_cola_normal": "Turnos en cola normal",
        "en_cola_prioridad": "Turnos en cola de prioridad",
        "atendidos_o_cancelados": "Atendidos / cancelados (historial)",
        "total_generados": "Total de turnos generados",
        "altura_arbol_historial": "Altura del árbol de historial",
    }

    contenedor = ctk.CTkFrame(frame_principal, fg_color="transparent")
    contenedor.pack(pady=10)

    for clave, etiqueta in etiquetas.items():
        fila = ctk.CTkFrame(contenedor)
        fila.pack(fill="x", pady=6, padx=20)
        ctk.CTkLabel(fila, text=etiqueta, font=("Arial", 15), width=320, anchor="w").pack(side="left", padx=10)
        ctk.CTkLabel(fila, text=str(m[clave]), font=("Arial", 16, "bold")).pack(side="left")

    ctk.CTkButton(frame_principal, text="Actualizar", command=mostrar_dashboard, width=150).pack(pady=20)


# =========================
# MENÚ LATERAL
# =========================

ctk.CTkLabel(frame_menu, text="MENÚ", font=("Arial", 26, "bold")).pack(pady=(20, 30))

botones_menu = [
    ("Inicio", mostrar_inicio),
    ("Nuevo Turno", mostrar_nuevo_turno),
    ("Atender / Cancelar", mostrar_atender_turnos),
    ("Ver Colas", mostrar_colas),
    ("Historial", mostrar_historial),
    ("Buscar (Árbol)", mostrar_buscar),
    ("Visualizar Árbol", mostrar_visualizacion_arbol),
    ("Dashboard", mostrar_dashboard),
]

for texto, comando in botones_menu:
    ctk.CTkButton(frame_menu, text=texto, command=comando, width=180).pack(pady=6, padx=15)

ctk.CTkButton(frame_menu, text="Salir", command=ventana.destroy,
              fg_color="red", hover_color="darkred", width=180).pack(pady=(40, 15), padx=15)

# =========================
# PANTALLA INICIAL Y EJECUCIÓN
# =========================

mostrar_inicio()
ventana.mainloop()
