from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

class WineInfoScreen(ctk.CTkToplevel):
    def __init__(self, master, wine_data):
        super().__init__(master)
        print(wine_data)
        self.title("Información del Vino")
        self.geometry("800x600")
        self.configure(fg_color="#F5F5F5")

        # Datos del vino
        self.name = wine_data[1] if wine_data[1] is not None else 'Desconocido'
        self.grape = wine_data[2] if wine_data[2] is not None else 'Desconocido'
        self.winery = wine_data[3] if wine_data[3] is not None else 'Desconocido'
        self.region = wine_data[4] if wine_data[4] is not None else 'Desconocido'
        self.vintage = wine_data[5] if wine_data[5] is not None else 'Desconocido'
        self.description = wine_data[6] if wine_data[6] is not None else 'Descripción no disponible'
        self.price = wine_data[7] if wine_data[7] is not None else 'No disponible'
        self.rating = wine_data[8] if wine_data[8] is not None else 'No calificado'
        self.image_path = wine_data[9]  # Ruta a la imagen del vino

        # Crear los widgets de la pantalla
        self.create_widgets()

    def create_widgets(self):
        # Encabezado
        header_frame = ctk.CTkFrame(self, fg_color="#4A0E0E", corner_radius=10)
        header_frame.pack(padx=20, pady=(20, 10), fill="x")

        title_label = ctk.CTkLabel(
            header_frame,
            text=self.name,
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#FFFFFF"
        )
        title_label.pack(padx=20, pady=10)

        # Imagen del vino
        if self.image_path:
            img = Image.open(self.image_path)
            img = img.resize((300, 300), Image.ANTIALIAS)
            img_tk = ImageTk.PhotoImage(img)

            img_label = ctk.CTkLabel(
                self,
                image=img_tk,
                text="",
                fg_color="#F5F5F5",
                corner_radius=10
            )
            img_label.image = img_tk
            img_label.pack(pady=10)

        # Información del vino
        info_frame = ctk.CTkFrame(self, fg_color="#4A0E0E", corner_radius=10)
        info_frame.pack(padx=20, pady=10, fill="x")

        labels = {
            "Cepa": self.grape,
            "Bodega": self.winery,
            "Región": self.region,
            "Añada": self.vintage,
            "Descripción": self.description,
            "Precio": f"{self.price} €",
            "Calificación": f"{self.rating}/5"
        }

        for key, value in labels.items():
            if value:  # Solo mostrar el label si el valor no es vacío
                label = ctk.CTkLabel(
                    info_frame,
                    text=f"{key}: {value}",
                    font=ctk.CTkFont(size=16, weight="bold"),
                    text_color="#FFFFFF"
                )
                label.pack(padx=20, pady=5, anchor="w")

        # Botones de acción
        action_frame = ctk.CTkFrame(self, fg_color="#F5F5F5", corner_radius=10)
        action_frame.pack(padx=20, pady=20, fill="x")

        add_favorite_button = ctk.CTkButton(
            action_frame,
            text="Añadir a favoritos",
            fg_color="#800020",
            hover_color="#FFD700",
            text_color="#FFFFFF",
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.add_to_favorites
        )
        add_favorite_button.pack(side="left", padx=10)

        close_button = ctk.CTkButton(
            action_frame,
            text="Cerrar",
            fg_color="#800020",
            hover_color="#FFD700",
            text_color="#FFFFFF",
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.destroy
        )
        close_button.pack(side="right", padx=10)

    def add_to_favorites(self):
        # Código para añadir el vino a favoritos
        print(f"Vino añadido a favoritos: {self.name}")
        self.destroy()
