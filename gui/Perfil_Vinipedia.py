import customtkinter as ctk

DARK_BURGUNDY = "#4A0E0E"
LIGHT_BURGUNDY = "#800020"
GOLD = "#FFD700"
CREAM = "#FFFDD0"
class Perfil_Programa:
    def __init__(self,root,show_perfil_frame,load_photo):
        self.colors = {
            "DARK_BURGUNDY": DARK_BURGUNDY,
            "LIGHT_BURGUNDY": LIGHT_BURGUNDY,
            "gold": GOLD,
            "cream": CREAM,
        }
        
        self.create_widgets(root,show_perfil_frame)
 
    def create_widgets(self,root,show_perfil_frame):
        # frame principal
        self.frame_principal_perfil = ctk.CTkFrame(
                    root,
                    fg_color = self.colors["DARK_BURGUNDY"],
                    border_width = 2,
                    border_color = self.colors["cream"],
                )
        self.frame_principal_perfil.pack(fill="both", expand=True, padx=0, pady=0)
        
        # boton exit
        frame_boton_exit = ctk.CTkFrame(self.frame_principal_perfil, fg_color=self.colors["DARK_BURGUNDY"])
        frame_boton_exit.pack(fill="x", pady=(5, 8),padx = 5)
 
        btn_back = ctk.CTkButton(frame_boton_exit, text="Volver", corner_radius=5, command=lambda :show_perfil_frame(self.frame_principal_perfil), width=0, fg_color=self.colors["gold"], text_color="black")
        btn_back.pack(side="left")
        
