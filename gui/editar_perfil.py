import customtkinter as ctk
from PIL import Image

DARK_BURGUNDY = "#4A0E0E"
LIGHT_BURGUNDY = "#800020"
GOLD = "#FFD700"
CREAM = "#FFFDD0"

user_data = {
    "name": "Ramiro",
    "fav_wine": "Malbec",
    "profile_picture": "path_to_profile_image"
}

class Perfil_Programa:
    def __init__(self, root, show_perfil_frame, load_photo):
        self.colors = {
            "DARK_BURGUNDY": DARK_BURGUNDY,
            "LIGHT_BURGUNDY": LIGHT_BURGUNDY,
            "gold": GOLD,
            "cream": CREAM,
        }
        
        self.x_root = 700
        self.y_root = 650
        
        self.root = root
        self.load_photo = load_photo
        self.create_widgets(root, show_perfil_frame)

    def create_widgets(self, root, show_perfil_frame):
        self.frame_principal_perfil = ctk.CTkFrame(
            root,
            fg_color=self.colors["DARK_BURGUNDY"],
            border_width=2,
            border_color=self.colors["cream"],
            width=self.x_root,
            height=self.y_root
        )
        self.frame_principal_perfil.pack(fill="both", expand=True, padx=0, pady=0)

        # Botón exit
        frame_boton_exit = ctk.CTkFrame(self.frame_principal_perfil, fg_color=self.colors["DARK_BURGUNDY"])
        frame_boton_exit.pack(fill="x", pady=(5, 8), padx=5)

        btn_back = ctk.CTkButton(frame_boton_exit, text="Volver", corner_radius=5,
                                 command=lambda: show_perfil_frame(self.frame_principal_perfil), width=0,
                                 fg_color=self.colors["gold"], text_color="black")
        btn_back.pack(side="left")

        # Información del perfil
        self.create_profile_field("Nombre", user_data["name"], self.frame_principal_perfil, lambda: self.edit_field("name"))
        self.create_profile_field("Vino Favorito", user_data["fav_wine"], self.frame_principal_perfil, lambda: self.edit_field("fav_wine"))
        self.create_profile_field("Foto de Perfil", "Cambiar imagen", self.frame_principal_perfil, lambda: self.edit_field("profile_picture"))

    def create_profile_field(self, label_text, field_text, parent_frame, edit_command):
        frame_field = ctk.CTkFrame(parent_frame, fg_color=self.colors["DARK_BURGUNDY"])
        frame_field.pack(fill="x", pady=10, padx=10)
        
        label = ctk.CTkLabel(frame_field, text=f"{label_text}: {field_text}", anchor="w", text_color=self.colors["cream"])
        label.pack(side="left", expand=True, fill="x")
        
        btn_edit = ctk.CTkButton(frame_field, text="...", corner_radius=5, width=30, fg_color=self.colors["gold"], 
                                 text_color="black", command=edit_command)
        btn_edit.pack(side="right")

    def edit_field(self, field_name):
        self.floating_frame = ctk.CTkFrame(self.frame_principal_perfil, fg_color=self.colors["LIGHT_BURGUNDY"], width=400, height=200)
        self.floating_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        label_edit = ctk.CTkLabel(self.floating_frame, text=f"Editar {field_name.capitalize()}", text_color=self.colors["cream"])
        label_edit.pack(pady=10)
        
        if field_name == "profile_picture":
            # Para editar la imagen de perfil
            btn_choose_image = ctk.CTkButton(self.floating_frame, text="Elegir Imagen", fg_color=self.colors["gold"], 
                                             text_color="black", command=self.choose_image)
            btn_choose_image.pack(pady=10)
        else:
            self.entry_edit = ctk.CTkEntry(self.floating_frame, fg_color=self.colors["cream"], text_color="black")
            self.entry_edit.pack(pady=10)
            
            # Botón para confirmar el cambio
            btn_confirm = ctk.CTkButton(self.floating_frame, text="Guardar", fg_color=self.colors["gold"], 
                                        text_color="black", command=lambda: self.save_changes(field_name))
            btn_confirm.pack(pady=10)
        
        # Botón para cerrar el frame flotante
        btn_close = ctk.CTkButton(self.floating_frame, text="Cerrar", fg_color=self.colors["gold"], 
                                  text_color="black", command=self.close_floating_frame)
        btn_close.pack(pady=10)

    def choose_image(self):
        # Aquí se colocaría la lógica para seleccionar la imagen
        user_data["profile_picture"] = "new_image_path"
        print("Imagen de perfil actualizada")

    def save_changes(self, field_name):
        new_value = self.entry_edit.get()
        user_data[field_name] = new_value
        print(f"{field_name} actualizado: {new_value}")
        self.close_floating_frame()

    def close_floating_frame(self):
        if self.floating_frame:
            self.floating_frame.destroy()

# Ejemplo de uso
root = ctk.CTk()
app = Perfil_Programa(root, lambda frame: frame.pack_forget(), None)
root.mainloop()