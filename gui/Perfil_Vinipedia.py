import customtkinter as ctk


DARK_BURGUNDY = "#4A0E0E"
LIGHT_BURGUNDY = "#800020"
GOLD = "#FFD700"
CREAM = "#FFFDD0"


class Perfil_Programa:
    def __init__(self,root,show_perfil_frame,user_data):
        self.colors = {
            "DARK_BURGUNDY": DARK_BURGUNDY,
            "LIGHT_BURGUNDY": LIGHT_BURGUNDY,
            "gold": GOLD,
            "cream": CREAM,
        }
        
        self.create_widgets(root,show_perfil_frame,user_data)
 
    def create_widgets(self,root,show_perfil_frame,user_data):
        # frame principal
        self.frame_principal_perfil = ctk.CTkFrame(
            root,
            fg_color=self.colors["DARK_BURGUNDY"],
            border_width=2,
            border_color=self.colors["cream"],
        )
        self.frame_principal_perfil.pack(fill="both", expand=True, padx=0, pady=0)

        # frame para el botón de salida
        self.frame_boton_exit = ctk.CTkFrame(self.frame_principal_perfil, fg_color=self.colors["DARK_BURGUNDY"])
        self.frame_boton_exit.pack(fill="x", pady=(5, 8), padx=5)
        #imagen editar
        self.photo_m()
        # etiqueta y campo de nombre
        self.name_label = ctk.CTkLabel(self.frame_principal_perfil, text="Nombre", text_color=GOLD)
        self.name_label.pack(side = "left",pady=5)
        self.name_entry = ctk.CTkEntry(self.frame_principal_perfil)
        self.name_entry.insert(0, user_data["name"])  # Cargar nombre desde user_data
        self.name_entry.pack(side= "left",padx=0, pady=0)

        # etiqueta y campo de biografía
        self.bio_label = ctk.CTkLabel(self.frame_principal_perfil, text="Biografía", text_color=GOLD)
        self.bio_label.pack(side = "left",pady=5)
        self.bio_entry = ctk.CTkEntry(self.frame_principal_perfil)
        self.bio_entry.insert(0, user_data["bio"])  # Cargar biografía desde user_data
        self.bio_entry.pack(side = "left",pady=10)

        # etiqueta y campo de vino favorito
        self.fav_wine_label = ctk.CTkLabel(self.frame_principal_perfil, text="Vino Favorito", text_color=GOLD)
        self.fav_wine_label.pack(side = "left",pady=5)
        self.fav_wine_entry = ctk.CTkEntry(self.frame_principal_perfil)
        self.fav_wine_entry.insert(0, user_data["fav_wine"])  # Cargar vino favorito desde user_data
        self.fav_wine_entry.pack(side = "left",pady=10)

        # botón de volver
        self.btn_back = ctk.CTkButton(
            self.frame_boton_exit, text="Volver", corner_radius=5,
            command=lambda: show_perfil_frame(self.frame_principal_perfil), 
            width=0, fg_color=self.colors["gold"], text_color="black"
        )
        self.btn_back.pack(side="left")
    def photo_m(self):
        self.photo_frame = ctk.CTkFrame(
            self.frame_principal_perfil,
            width=150,
            height=150,
            corner_radius=75,  # Ensures the frame is circular
            fg_color=self.colors["DARK_BURGUNDY"],
        )
        self.photo_frame.place(relx=0.5, rely=0.2, anchor="center")

        self.canvas = ctk.CTkCanvas(
            self.photo_frame,
            width=70,
            height=70,
            bg=self.colors["DARK_BURGUNDY"],
            highlightthickness=0,
        )
        self.canvas.pack(fill="both", expand=True)

        # Cargar la imagen predeterminada
        self.load_default_photo()

        # Load profile photo button
        self.load_photo_button = ctk.CTkButton(
            self.frame_principal_perfil,
            text="Cargar Imagen",
            command=self.load_photo,
            fg_color=self.colors["LIGHT_BURGUNDY"],
            hover_color=self.colors["gold"],
        )
        self.load_photo_button.place(relx=0.5, rely=0.35, anchor="center")
