import customtkinter as ctk
from PIL import Image, ImageTk
from perfil import WineAppMobileGUI
# Paleta de colores
DARK_BURGUNDY = "#4A0E0E"
LIGHT_BURGUNDY = "#800020"
GOLD = "#FFD700"
CREAM = "#FFFDD0"

class WineAppHomeGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Wine App")
        self.geometry("800x600")
        self.configure(fg_color=DARK_BURGUNDY)

        # Configura el diseño de la grilla
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Crea la barra lateral
        self.create_sidebar()

        # Crea el área de contenido principal
        self.create_main_content()

    def create_sidebar(self):
        sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color=DARK_BURGUNDY)
        sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")
        sidebar.grid_rowconfigure(8, weight=1)

        logo_label = ctk.CTkLabel(sidebar, text="Aplicación de Vinos", font=ctk.CTkFont(size=20, weight="bold"), text_color=GOLD)
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        buttons = [
            ("Inicio", self.home_event),
            ("Perfil", self.profile_event),
            ("Subir opinión", self.upload_opinion_event),
            ("Soporte", self.support_event)
        ]

        for i, (text, command) in enumerate(buttons, start=1):
            button = ctk.CTkButton(sidebar, text=text, command=command, fg_color=LIGHT_BURGUNDY, hover_color=GOLD, text_color=CREAM)
            button.grid(row=i, column=0, padx=20, pady=10, sticky="ew")

    def create_main_content(self):
        main_frame = ctk.CTkFrame(self, fg_color=CREAM)
        main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)

        # Barra de búsqueda
        search_frame = ctk.CTkFrame(main_frame, fg_color=LIGHT_BURGUNDY)
        search_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        search_entry = ctk.CTkEntry(search_frame, placeholder_text="Buscar por: nombre, cepa, bodega, región, añada", fg_color=CREAM, text_color=DARK_BURGUNDY)
        search_entry.pack(side="left", expand=True, fill="x", padx=(10, 10))
        search_button = ctk.CTkButton(search_frame, text="Buscar", width=100,fg_color=GOLD, hover_color=DARK_BURGUNDY, text_color=DARK_BURGUNDY)
        search_button.pack(side="right", padx=(0, 10), pady=10)

        # Contenido principal (placeholder para la información del vino)
        content_frame = ctk.CTkFrame(main_frame, fg_color=LIGHT_BURGUNDY)
        content_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        content_label = ctk.CTkLabel(content_frame, text="Información del vino y opciones aparecerán aquí", wraplength=400, text_color="#b32222")
        content_label.pack(expand=True)

        # Botones de acción
        action_frame = ctk.CTkFrame(main_frame, fg_color=CREAM)
        action_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        add_favorite_button = ctk.CTkButton(action_frame, text="Añadir a favoritos", command=self.add_favorite_event, fg_color=LIGHT_BURGUNDY, hover_color=GOLD, text_color=CREAM)
        add_favorite_button.pack(side="left", padx=5)
        view_info_button = ctk.CTkButton(action_frame, text="Ver información del vino", command=self.view_info_event, fg_color=LIGHT_BURGUNDY, hover_color=GOLD, text_color=CREAM)
        view_info_button.pack(side="right", padx=5)

    def home_event(self):
        self.destroy()
        self.__init__()

    def guided_tasting_event(self):
        print("Botón de cata guiada presionado")


    def profile_event(self):
        profile = WineAppMobileGUI()
        profile.run()

    def upload_opinion_event(self):
        print("Botón de subir opinión presionado")

    def support_event(self):
        print("Botón de soporte presionado")

    def add_favorite_event(self):
        print("Botón de agregar a favoritos presionado")

    def view_info_event(self):
        print("Botón de ver información del vino presionado")

    def buy_event(self):
        print("Botón de comprar presionado")

if __name__ == "__main__":
    app = WineAppHomeGUI()
    app.mainloop()
