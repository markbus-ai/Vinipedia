import customtkinter as ctk
from dropdown_menu import WineAppDropdownMenu

DARK_BURGUNDY = "#4A0E0E"
LIGHT_BURGUNDY = "#800020"
GOLD = "#FFD700"
CREAM = "#FFFDD0"
TEXT_COLOR = "#000000"

class Formulario:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Soporte Al Cliente")
        self.window.geometry("500x600")
        self.window.configure(fg_color=DARK_BURGUNDY)
        # Add the dropdown menu
        self.dropdown_menu = WineAppDropdownMenu(self.window, current_page=self.window)
        self.dropdown_menu.pack(anchor="nw", padx=10, pady=10)

        label_title = ctk.CTkLabel(self.window, text="Formulario de Soporte al Cliente", font=("Helvetica", 20, "bold"), text_color=GOLD)
        label_title.pack(pady=10)

        label_nombre = ctk.CTkLabel(self.window, text="Nombre:", font=("Helvetica", 14), text_color=CREAM)
        label_nombre.pack(pady=(10, 0), anchor="w", padx=20)
        self.entry_nombre = ctk.CTkEntry(self.window, placeholder_text="Ingrese su nombre", fg_color=CREAM, text_color=TEXT_COLOR)
        self.entry_nombre.pack(pady=(0, 10), padx=20, fill="x")

        label_correo = ctk.CTkLabel(self.window, text="Correo Electrónico:", font=("Helvetica", 14), text_color=CREAM)
        label_correo.pack(pady=(10, 0), anchor="w", padx=20)
        self.entry_correo = ctk.CTkEntry(self.window, placeholder_text="Ingrese su correo electrónico", fg_color=CREAM, text_color=TEXT_COLOR)
        self.entry_correo.pack(pady=(0, 10), padx=20, fill="x")

        label_asunto = ctk.CTkLabel(self.window, text="Asunto:", font=("Helvetica", 14), text_color=CREAM)
        label_asunto.pack(pady=(10, 0), anchor="w", padx=20)
        self.entry_asunto = ctk.CTkEntry(self.window, placeholder_text="Ingrese el asunto", fg_color=CREAM, text_color=TEXT_COLOR)
        self.entry_asunto.pack(pady=(0, 10), padx=20, fill="x")

        label_mensaje = ctk.CTkLabel(self.window, text="Mensaje:", font=("Helvetica", 14), text_color=CREAM)
        label_mensaje.pack(pady=(10, 0), anchor="w", padx=20)
        self.text_mensaje = ctk.CTkTextbox(self.window, height=200, fg_color=CREAM, text_color=TEXT_COLOR)
        self.text_mensaje.pack(pady=(0, 10), padx=20, fill="both", expand=True)

        btn_enviar = ctk.CTkButton(self.window, text="Enviar", command=self.enviar, fg_color=LIGHT_BURGUNDY, hover_color=DARK_BURGUNDY, text_color=CREAM)
        btn_enviar.pack(pady=10, padx=20, side="bottom", anchor="s")

    def enviar(self):
        print("Datos enviados:")
        print(f"Nombre: {self.entry_nombre.get()}")
        print(f"Correo Electrónico: {self.entry_correo.get()}")
        print(f"Asunto: {self.entry_asunto.get()}")
        print(f"Mensaje: {self.text_mensaje.get('1.0', 'end').strip()}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = Formulario()
    app.run()