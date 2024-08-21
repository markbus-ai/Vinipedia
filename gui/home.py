import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import subprocess
import sqlite3

# Colores de la paleta personalizada
DARK_BURGUNDY = "#4A0E0E"
LIGHT_BURGUNDY = "#800020"
GOLD = "#FFD700"
CREAM = "#FFFDD0"

class WineAppHomeGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.db_path = os.path.join(os.path.dirname(__file__), '..', 'DB', 'wines.db')

        self.title("Wine App")
        self.geometry("1024x768")
        self.configure(fg_color=DARK_BURGUNDY)

        # Configuración de la grilla para un diseño responsivo
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Menú desplegable lateral
        self.create_sidebar()

        # Área principal de contenido
        self.create_main_content()

        # Verificación inicial de la base de datos
        self.verify_database()

    def create_sidebar(self):
        sidebar = ctk.CTkFrame(self, width=250, corner_radius=0, fg_color=DARK_BURGUNDY)
        sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")
        sidebar.grid_rowconfigure(8, weight=1)

        logo_label = ctk.CTkLabel(sidebar, text="Vinipedia", font=ctk.CTkFont(size=24, weight="bold"), text_color=GOLD)
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        buttons = [
            ("Inicio", self.home_event),
            ("Perfil", self.profile_event),
            ("Mapa de bodegas", self.map_event),
            ("Soporte", self.support_event)
        ]

        for i, (text, command) in enumerate(buttons, start=1):
            button = ctk.CTkButton(
                sidebar, text=text, command=command,
                fg_color=LIGHT_BURGUNDY, hover_color=GOLD, text_color=CREAM,
                font=ctk.CTkFont(size=16, weight="bold")
            )
            button.grid(row=i, column=0, padx=20, pady=10, sticky="ew")

    def create_main_content(self):
        self.main_frame = ctk.CTkFrame(self, fg_color=CREAM)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # Barra de búsqueda
        search_frame = ctk.CTkFrame(self.main_frame, fg_color=LIGHT_BURGUNDY, corner_radius=10)
        search_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        self.search_entry = ctk.CTkEntry(
            search_frame, 
            placeholder_text="Buscar por: nombre, cepa, bodega, región, añada", 
            fg_color=CREAM, text_color=DARK_BURGUNDY,
            font=ctk.CTkFont(size=14)
        )
        self.search_entry.pack(side="left", expand=True, fill="x", padx=(10, 10))
        
        search_button = ctk.CTkButton(
            search_frame, text="Buscar", width=120,
            fg_color=GOLD, hover_color=DARK_BURGUNDY, text_color=DARK_BURGUNDY,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.search_event
        )
        search_button.pack(side="right", padx=(0, 10), pady=10)

        # Área de contenido para los resultados
        self.content_frame = ctk.CTkFrame(self.main_frame, fg_color=LIGHT_BURGUNDY, corner_radius=10)
        self.content_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        self.content_label = ctk.CTkLabel(
            self.content_frame, 
            text="Información del vino y opciones aparecerán aquí", 
            wraplength=500, text_color=GOLD,
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.content_label.pack(expand=True, padx=20, pady=20)

        # Botones de acción
        action_frame = ctk.CTkFrame(self.main_frame, fg_color=CREAM, corner_radius=10)
        action_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        
        add_favorite_button = ctk.CTkButton(
            action_frame, text="Añadir a favoritos",
            fg_color=LIGHT_BURGUNDY, hover_color=GOLD, text_color=CREAM,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.add_favorite_event
        )
        add_favorite_button.pack(side="left", padx=5)

        view_info_button = ctk.CTkButton(
            action_frame, text="Ver información del vino",
            fg_color=LIGHT_BURGUNDY, hover_color=GOLD, text_color=CREAM,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.view_info_event
        )
        view_info_button.pack(side="right", padx=5)

    def search_event(self):
        query = self.search_entry.get()
        if query:
            results = self.search_database(query)
            self.display_search_results(results)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese un término de búsqueda.")

    def search_database(self, query):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Wines WHERE name LIKE ?", ('%' + query + '%',))
        results = cursor.fetchall()
        conn.close()
        return results

    def display_search_results(self, results):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        if results:
            for result in results:
                wine_frame = ctk.CTkFrame(self.content_frame, fg_color=CREAM, corner_radius=10)
                wine_frame.pack(pady=10, padx=10, fill="x")

                name_label = ctk.CTkLabel(
                    wine_frame, text=f"🍷 {result[1]}", 
                    font=ctk.CTkFont(size=18, weight="bold"), 
                    text_color=LIGHT_BURGUNDY
                )
                name_label.pack(pady=(10, 5))

                details_label = ctk.CTkLabel(
                    wine_frame, 
                    text=f"Cepa: {result[2]}  |  Bodega: {result[3]}  |  Región: {result[4]}  |  Añada: {result[5]}", 
                    text_color=DARK_BURGUNDY,
                    wraplength=700,
                    justify="left"
                )
                details_label.pack(pady=5)

                action_frame = ctk.CTkFrame(wine_frame, fg_color=CREAM)
                action_frame.pack(pady=(5, 10), fill="x")

                add_favorite_button = ctk.CTkButton(
                    action_frame, 
                    text="⭐ Añadir a favoritos", 
                    command=lambda wine=result: self.add_favorite_event(wine), 
                    fg_color=GOLD, 
                    hover_color=LIGHT_BURGUNDY, 
                    text_color=DARK_BURGUNDY
                )
                add_favorite_button.pack(side="left", padx=5)

                view_info_button = ctk.CTkButton(
                    action_frame, 
                    text="🔍 Ver información", 
                    command=lambda wine=result: self.view_info_event(wine), 
                    fg_color=GOLD, 
                    hover_color=LIGHT_BURGUNDY, 
                    text_color=DARK_BURGUNDY
                )
                view_info_button.pack(side="right", padx=5)
        else:
            no_result_label = ctk.CTkLabel(
                self.content_frame, 
                text="❌ No se encontraron resultados", 
                wraplength=400, 
                text_color=GOLD,
                font=ctk.CTkFont(size=16, weight="bold")
            )
            no_result_label.pack(pady=5)

    def verify_database(self):
        if not os.path.exists(self.db_path):
            messagebox.showerror("Error", "La base de datos no se encontró.")
            self.destroy()

    def home_event(self):
        self.destroy()
        print("Botón de inicio presionado")
        subprocess.run(["python", "gui/home.py"])

    def profile_event(self):
        self.destroy()
        subprocess.run(["python", "gui/perfil.py"])
        print("Botón de perfil presionado")

    def upload_opinion_event(self):
        print("Botón de subir opinión presionado")

    def support_event(self):
        self.destroy()
        subprocess.run(["python", "gui/suporte.py"])
        print("Botón de soporte presionado")

    def map_event(self):
        self.destroy()
        subprocess.run(["python", "gui/mapa.py"])
        print("Botón de mapa presionado")

    def add_favorite_event(self, wine):
        # Código para añadir el vino a favoritos
        print(f"Vino añadido a favoritos: {wine[1]}")

    def view_info_event(self, wine):
        # Código para ver la información del vino
        print(f"Ver información del vino: {wine[1]}")

# Ejecuta la aplicación
if __name__ == "__main__":
    app = WineAppHomeGUI()
    app.mainloop()
