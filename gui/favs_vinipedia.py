import customtkinter as ctk
from tkinter import messagebox
import os

class FavtsPrograma:
    def __init__(self,root,show_perfil_frame):
        self.Nombres_Vinos = "gui/datos_favts/nombre_vinos.txt"
        self.Favoritos_Vinos = "gui/datos_favts/favoritos_vinos.txt"
 
        self.vinos_favoritos = self.cargar_favoritos_vinos()
 
        self.DARK_BURGUNDY = "#4A0E0E"
        self.LIGHT_BURGUNDY = "#800020"
        self.GOLD = "#FFD700"
        self.CREAM = "#FFFDD0"
 
        self.colors = {
            "DARK_BURGUNDY": self.DARK_BURGUNDY,
            "LIGHT_BURGUNDY": self.LIGHT_BURGUNDY,
            "gold": self.GOLD,
            "cream": self.CREAM,
        }
 
        self.create_widgets(root,show_perfil_frame)
        self.mostrar_favoritos()
 
    def leer_nombre_vinos(self):
        with open(self.Nombres_Vinos, "r", encoding='utf-8') as file:
            return [line.strip().split(',') for line in file if line.strip()]
 
    def cargar_favoritos_vinos(self):
        if os.path.exists(self.Favoritos_Vinos):
            with open(self.Favoritos_Vinos, "r", encoding='utf-8') as file:
                return [eval(line.strip()) for line in file if line.strip()]
        return []
 
    def guardar_favts(self):
        with open(self.Favoritos_Vinos, "w", encoding='utf-8') as file:
            for vino in self.vinos_favoritos:
                file.write(f"{vino}\n")
 
    def agregar_vino(self):
        vino_seleccionado = self.combo_vinos.get()
        if vino_seleccionado:
            vino_info = next((v for v in self.leer_nombre_vinos() if v[0] == vino_seleccionado), None)
            if vino_info:
                estrellas = int(self.slider_estrellas.get())
                vino = tuple(vino_info + [estrellas])
                self.vinos_favoritos.append(vino)
                self.guardar_favts()
                self.mostrar_favoritos()
                self.combo_vinos.set('')
                self.slider_estrellas.set(3)
                self.frame_flotante.place_forget()
            else:
                messagebox.showwarning("Advertencia", "Vino no encontrado")
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un vino")
 
    def mostrar_favoritos(self, filtro=None):
        for widget in self.frame_vinos_interno.winfo_children():
            widget.destroy()
 
        label_favoritos_titulo = ctk.CTkLabel(
            self.frame_vinos_interno,
            text="Vinos Favoritos:",
            font=('Arial', 18, 'bold'),
            text_color=self.colors["gold"]
        )
        label_favoritos_titulo.pack(pady=10)
 
        vinos_a_mostrar = self.vinos_favoritos.copy()
        if filtro:
            vinos_a_mostrar = [vino for vino in self.vinos_favoritos if filtro.lower() in vino[0].lower()]
 
        if not vinos_a_mostrar:
            label_no_result = ctk.CTkLabel(
                self.frame_vinos_interno,
                text="No se encontraron vinos favoritos.",
                text_color=self.colors["gold"],
                font=('Arial', 14)
            )
            label_no_result.pack(pady=20)
            return
 
        for vino in vinos_a_mostrar:
            contenedor = ctk.CTkFrame(
                self.frame_vinos_interno,
                fg_color=self.colors["LIGHT_BURGUNDY"],
                corner_radius=10,
                border_width=2,
                border_color=self.colors["gold"]
            )
            contenedor.pack(pady=10, padx=20, fill="x")
 
            label_nombre = ctk.CTkLabel(
                contenedor,
                text=f"{vino[0]} ({vino[2]})",
                text_color="white",
                font=('Arial', 16, 'bold')
            )
            label_nombre.pack(anchor="w", padx=10, pady=(10, 5))
 
            label_tipo = ctk.CTkLabel(
                contenedor,
                text=f"Tipo: {vino[1]}",
                text_color="white",
                font=('Arial', 12)
            )
            label_tipo.pack(anchor="w", padx=10, pady=2)
 
            label_bodega = ctk.CTkLabel(
                contenedor,
                text=f"Bodega: {vino[3]} - Región: {vino[4]}",
                text_color="white",
                font=('Arial', 12)
            )
            label_bodega.pack(anchor="w", padx=10, pady=2)
 
            label_pais_precio = ctk.CTkLabel(
                contenedor,
                text=f"País: {vino[5]} - Precio: ${vino[6]}",
                text_color="white",
                font=('Arial', 12)
            )
            label_pais_precio.pack(anchor="w", padx=10, pady=2)
 
            if len(vino) > 7:
                estrellas = int(vino[8])
 
                label_estrellas = ctk.CTkLabel(
                    contenedor,
                    text="★" * estrellas,
                    text_color=self.colors["gold"],
                    font=('Arial', 16)
                )
                label_estrellas.pack(anchor="w", padx=10, pady=(5, 10))
 
    def mostrar_frame_agregar_vino(self):
        self.frame_flotante.place(relx=0.5, rely=0.5, anchor="center")
 
    def mostrar_sugerencias(self, event=None):
        texto = self.entry_buscar.get().lower()
        sugerencias = [vino[0] for vino in self.leer_nombre_vinos() if texto in vino[0].lower()]
        self.combo_vinos['values'] = sugerencias
 
    def create_widgets(self,root,show_perfil_frame):
        # frame principal
        self.frame_favts = ctk.CTkFrame(
            root,
            fg_color=self.colors["DARK_BURGUNDY"],
            border_width=2,
            border_color=self.colors["cream"])
        
        self.frame_favts.pack(fill="both", expand=True, padx=0, pady=0)
        
        # boton exit
        frame_boton_exit = ctk.CTkFrame(self.frame_favts, fg_color=self.colors["DARK_BURGUNDY"])
        frame_boton_exit.pack(fill="x", pady=(5, 8),padx = 5)
 
        btn_back = ctk.CTkButton(
            frame_boton_exit,
            text="Volver",
            corner_radius=5,
            command=lambda :show_perfil_frame(self.frame_favts),
            width=0,
            fg_color=self.colors["gold"],
            text_color="black"
            )
        btn_back.pack(side="left")
 
        # titulo
        label_titulo = ctk.CTkLabel(
            self.frame_favts,
            text="Clasificación de Vinos",
            font=('Arial', 24, 'bold'),
            text_color=self.colors["gold"]
        )
        label_titulo.pack(pady=10)
 
        # frame para buscar y mostrar sugerencias
        frame_buscar = ctk.CTkFrame(self.frame_favts, fg_color=self.colors["DARK_BURGUNDY"])
        frame_buscar.pack(pady=10, fill="x", padx=10)

 
        # entry para buscar vino
        self.entry_buscar = ctk.CTkEntry(
            frame_buscar,
            placeholder_text="Buscar Vino",
            width=250,
            font=('Arial', 14)
        )
        self.entry_buscar.pack(side="left", padx=(20, 0), expand=True, anchor="center",fill="both")
        self.entry_buscar.bind("<KeyRelease>", self.mostrar_sugerencias)
 
        # botón para confirmar la búsqueda
        boton_buscar = ctk.CTkButton(
            frame_buscar, text="Buscar",
            command=lambda: self.mostrar_favoritos(self.entry_buscar.get()),
            fg_color=self.colors["gold"],
            text_color="black",
            width=100
            )
        
        boton_buscar.pack(padx = (10,20),side="left", anchor="center",fill="both")
 
        # Frame para la lista de vinos favoritos
        lista_vinos_frame = ctk.CTkFrame(self.frame_favts, fg_color=self.colors["DARK_BURGUNDY"])
        lista_vinos_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Scrollbar para la lista de vinos favoritos
        scrollbar = ctk.CTkScrollbar(lista_vinos_frame, width=10)
        scrollbar.pack(side="right", fill="y")

        # Canvas para contener los vinos favoritos y permitir scroll
        self.canvas_vinos = ctk.CTkCanvas(lista_vinos_frame, bg=self.colors["DARK_BURGUNDY"], highlightthickness=0)
        self.canvas_vinos.pack(side="left", fill="both", expand=True)

        # Configurar el scrollbar
        scrollbar.configure(command=self.canvas_vinos.yview)
        self.canvas_vinos.configure(yscrollcommand=scrollbar.set)

        # Frame interno para los vinos favoritos
        self.frame_vinos_interno = ctk.CTkFrame(self.canvas_vinos, fg_color=self.colors["DARK_BURGUNDY"])
        self.canvas_vinos.create_window((0, 0), window=self.frame_vinos_interno, anchor="nw")
 
        # frame flotante para agregar un nuevo vino
        self.frame_flotante = ctk.CTkFrame(
            root,
            fg_color=self.colors["DARK_BURGUNDY"],
            corner_radius=10,
            border_width=2,
            border_color=self.colors["gold"]
        )
 
        label_titulo_agregar = ctk.CTkLabel(
            self.frame_flotante,
            text="Agregar Nuevo Vino",
            font=('Arial', 16, 'bold'),
            text_color="white"
        )
        label_titulo_agregar.grid(row=0, column=0, columnspan=2, pady=10)
 
        label_vino = ctk.CTkLabel(self.frame_flotante, text="Seleccionar Vino:", text_color="white", font=('Arial', 12))
        label_vino.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.combo_vinos = ctk.CTkComboBox(
            self.frame_flotante,
            values=[vino[0] for vino in self.leer_nombre_vinos()],
            width=200,
            font=('Arial', 12)
        )
        self.combo_vinos.grid(row=1, column=1, padx=5, pady=5, sticky="w")
 
        label_estrellas = ctk.CTkLabel(self.frame_flotante, text="Calificación:", text_color="white", font=('Arial', 12))
        label_estrellas.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.slider_estrellas = ctk.CTkSlider(
            self.frame_flotante,
            from_=1,
            to=5,
            number_of_steps=4,
            width=200,
            command=lambda value: self.actualizar_label_estrellas(value)
        )
        self.slider_estrellas.set(3)
        self.slider_estrellas.grid(row=2, column=1, padx=5, pady=5, sticky="w")
 
        self.label_estrellas_valor = ctk.CTkLabel(
            self.frame_flotante,
            text="★★★",
            text_color=self.colors["gold"],
            font=('Arial', 16)
            )
        self.label_estrellas_valor.grid(row=3, column=0, columnspan=2, pady=5)
 
        boton_agregar = ctk.CTkButton(
            self.frame_flotante,
            text="Agregar Vino",
            command=self.agregar_vino,
            fg_color=self.colors["gold"],
            text_color="black",
            hover_color=self.colors["LIGHT_BURGUNDY"],
            width=200,
            font=('Arial', 12, 'bold')
        )
        boton_agregar.grid(row=4, column=0, columnspan=2, pady=10)
 
        # botón para mostrar el frame flotante de agregar vino
        boton_abrir_agregar = ctk.CTkButton(
            self.frame_favts,
            text="Agregar Nuevo Vino",
            command=self.mostrar_frame_agregar_vino,
            fg_color=self.colors["gold"],
            text_color="black",
            hover_color=self.colors["LIGHT_BURGUNDY"],
            width=200,
            font=('Arial', 12, 'bold')
        )
        boton_abrir_agregar.pack(pady=10)
 
        # función para actualizar el tamaño del frame interno
        def actualizar_tamanio_frame(event):
            canvas_width = event.width
            self.canvas_vinos.itemconfig(self.canvas_vinos_window, width=canvas_width)

        self.canvas_vinos_window = self.canvas_vinos.create_window((0, 0), window=self.frame_vinos_interno, anchor="nw")
        self.canvas_vinos.bind("<Configure>", actualizar_tamanio_frame)

        # función para actualizar el área de scroll del canvas
        def actualizar_scrollregion(event):
            self.canvas_vinos.configure(scrollregion=self.canvas_vinos.bbox("all"))

        self.frame_vinos_interno.bind("<Configure>", actualizar_scrollregion)
    def actualizar_label_estrellas(self, value):
        estrellas = "★" * int(round(float(value)))
        self.label_estrellas_valor.configure(text=estrellas)