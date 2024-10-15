import sys
import json
import os
from PIL import Image, ImageTk, ImageDraw
import customtkinter as ctk
from tkinter import filedialog
from dropdown_menu import WineAppDropdownMenu
from favs_vinipedia import FavtsPrograma
from Perfil_Vinipedia import Perfil_Programa

# Color palette
DARK_BURGUNDY = "#4A0E0E"
LIGHT_BURGUNDY = "#800020"
GOLD = "#FFD700"
CREAM = "#FFFDD0"


class WineAppMobileGUI:
    def __init__(self, user = None):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")
        self.root = ctk.CTk()
        self.root.title("Wine Enthusiast Profile")
        #Centrar Ventana en la pantalla
        self.x_root = 700
        self.y_root = 650    #Cambiar x_root, y_root para ajustar resolucion de pantalla
        self.ubi_x=(self.root.winfo_screenwidth() // 2) - (self.x_root // 2)  
        self.ubi_y=(self.root.winfo_screenheight() // 4) - (self.y_root // 4)
        self.root.geometry(f"{self.x_root}x{self.y_root}+{self.ubi_x}+{self.ubi_y}")
        self.root.after(1,self.ventana_max)
        self.user = user
        print("USER: ",self.user)

        self.colors = {
            "DARK_BURGUNDY": DARK_BURGUNDY,
            "LIGHT_BURGUNDY": LIGHT_BURGUNDY,
            "gold": GOLD,
            "cream": CREAM,
        }

        # Ruta de la imagen predeterminada
        self.default_image_path = 'img/image.png'  # Asegúrate de que sea relativo al directorio del script
        self.create_widgets()
        self.layout_widgets()
        self.root.after(100, self.load_reviews)

    def ventana_max(self):
        self.root.state("zoom")
 
    def create_widgets(self):
        # Main content frame
        self.main_frame = ctk.CTkFrame(
            self.root,
            fg_color=self.colors["DARK_BURGUNDY"],
            border_width=2,
            border_color=self.colors["cream"],
        )
        self.main_frame.pack(fill="both", expand=True)

        # Add the dropdown menu
        self.dropdown_menu = WineAppDropdownMenu(
            self.main_frame, current_page=self.root
        )
        self.dropdown_menu.place(x=10, y=10)

        self.photo_main(self.main_frame)

        # Name
        self.confirm_user()  # muestra label

        # Favorite Wine
        self.show_fav_vino = ctk.CTkLabel(
            self.show_name_frame,
            text= f"Vino Favorito: {user_data["fav_wine"]}",                      
            height=80,
            font=("Helvetica", 24,"bold"),
            width=300,
            fg_color=self.colors["DARK_BURGUNDY"],
            text_color=self.colors["gold"],
        )


        # About
        self.about_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.about_label = ctk.CTkLabel(
            self.about_frame,
            text="Acerca de mí",
            font=("Helvetica", 16, "bold"),
            text_color=self.colors["gold"],
        )

        self.about_text = ctk.CTkTextbox(
            self.about_frame,
            wrap="word",
            height=80,
            font=("Helvetica", 14),
            width=300,
            fg_color=self.colors["cream"],
            text_color=self.colors["DARK_BURGUNDY"],
        )
        self.about_text.insert("1.0", "Comparte tu pasión por el vino...")
        self.about_text.bind("<Button-1>", lambda x: self.about_text.delete("1.0", ctk.END))

        # Last Reviews
        self.reviews_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.reviews_label = ctk.CTkLabel(
            self.reviews_frame,
            text="Reseñas recientes de vinos",
            font=("Helvetica", 16, "bold"),
            text_color=self.colors["gold"],
        )

        # Scrollbar para el textbox de reseñas
        self.scrollbar_review = ctk.CTkScrollbar(self.reviews_frame)

        # Buttons
        self.button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.add_review_button = ctk.CTkButton(
            self.button_frame,
            text="Agregar reseña",
            fg_color=self.colors["LIGHT_BURGUNDY"],
            hover_color=self.colors["gold"],
            command=self.show_add_review_frame,
        )

        self.view_more_button = ctk.CTkButton(
            self.button_frame,
            text="Ver más reseñas",
            fg_color=self.colors["LIGHT_BURGUNDY"],
            hover_color=self.colors["gold"],
            command=self.show_all_reviews_frame,
        )

        self.fav_button = ctk.CTkButton(
            self.button_frame,
            text="Favoritos",
            fg_color=self.colors["LIGHT_BURGUNDY"],
            hover_color=self.colors["gold"],
            command=self.show_favs,
        )

        self.edit_profile_button = ctk.CTkButton(
            self.button_frame,
            text="Editar perfil",
            fg_color=self.colors["LIGHT_BURGUNDY"],
            hover_color=self.colors["gold"],
            command=self.show_perfil,
        )

    #funcion mostral Label con nombre del usuario
    def confirm_user(self):    
        
        if self.user is not None:                            
            texto_confirm = f"Hola {self.user["name"]}!"                  
        else:
            texto_confirm = "Sin User"
        
        self.show_name_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.show_name = ctk.CTkLabel(
            self.show_name_frame,
            text=texto_confirm,                      
            height=80,
            font=("Helvetica", 24,"bold"),
            width=300,
            fg_color=self.colors["DARK_BURGUNDY"],
            text_color=self.colors["gold"],
        )


    def layout_widgets(self):
        '''self.show_name.place(relx=0.5, rely=0.45, anchor="center")'''
        self.show_name_frame.place(relx=0.5, rely=0.49, anchor="center")
        self.show_name.pack()
        self.show_fav_vino.pack()

        self.about_frame.place(relx=0.5, rely=0.65, anchor="center", relwidth=0.9)
        self.about_label.pack(anchor="w")
        self.about_text.pack(fill="x", pady=5)

        self.reviews_frame.place(relx=0.5, rely=0.8, anchor="center", relwidth=0.9)
        self.reviews_label.pack(anchor="w", pady=(0, 5))


        self.button_frame.place(relx=0.5, rely=0.94, anchor="center", relwidth=0.9)
        self.add_review_button.pack(side="left", expand=True, padx=5,pady = (20,0))
        self.view_more_button.pack(side="left", expand=True, padx=5,pady = (20,0))
        self.fav_button.pack(side="left", expand=True, padx=5,pady = (20,0))
        self.edit_profile_button.pack(side="right", expand=True, padx=5,pady = (20,0))
    
    def load_default_photo(self):
        """ Cargar la imagen predeterminada """
        try:
            img = Image.open(self.default_image_path)
            img = img.resize((150, 150), Image.Resampling.LANCZOS)

            # Crear la máscara circular
            mask = Image.new('L', (150, 150), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, 150, 150), fill=255)
            img.putalpha(mask)

            # Crear la imagen circular con fondo transparente
            circular_img = Image.new('RGBA', (150, 150), (0, 0, 0, 0))
            circular_img.paste(img, (0, 0), img)

            # Convertir a PhotoImage y mostrar en el canvas
            self.photo_img = ImageTk.PhotoImage(circular_img)
            self.canvas.create_image(75, 75, image=self.photo_img)
        except Exception as e:
            print(f"Error al cargar la imagen predeterminada: {e}")

    def load_photo(self):
        """ Cargar una foto de perfil """
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.png *.jpeg *.gif")]
        )
        if file_path:
            self.default_image_path = file_path
            self.load_default_photo()

    def load_reviews(self):
        """ Cargar reseñas de un archivo JSON """
        reviews_path = 'data/reviews.json'
        if os.path.exists(reviews_path):
            with open(reviews_path, 'r') as f:
                reviews = json.load(f)
                self.display_reviews(reviews)

    def display_reviews(self, reviews):
        """ Mostrar solo las últimas dos reseñas """

        # Limpiar los textboxes anteriores
        if hasattr(self, 'review_boxes'):
            for box in self.review_boxes:
                box.pack_forget()

        # Reiniciar la lista de review_boxes
        self.review_boxes = []

        # Mostrar las dos últimas reseñas
        reviews_to_display = reviews[-2:]  # Las dos últimas reseñas
        for review in reviews_to_display:
            box = ctk.CTkTextbox(
                self.reviews_frame,
                height=40,
                font=("Helvetica", 12),
                fg_color=self.colors["cream"],
                text_color=self.colors["DARK_BURGUNDY"],
            )
            box.insert(ctk.END, f"{review['wine_name']} ({review['year']}) - {review['review_text']}")
            box.pack(fill="x", pady=2)

            # Añadir el box a la lista
            self.review_boxes.append(box)

#Review
    def show_add_review_frame(self):
        """ Muestra un frame flotante para agregar una nueva reseña """
        self.add_review_frame = ctk.CTkFrame(
            self.main_frame, 
            fg_color=self.colors["DARK_BURGUNDY"],
            corner_radius=10,
            border_width=2,
            border_color=self.colors["gold"]
        )
        self.add_review_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.3)

        # Campo para ingresar el nombre del vino
        self.wine_name_entry = ctk.CTkEntry(self.add_review_frame, width=300, placeholder_text="Nombre del vino (e.g., Chardonnay)")
        self.wine_name_entry.pack(pady=10)

        # Campo para ingresar el año del vino
        self.wine_year_entry = ctk.CTkEntry(self.add_review_frame, width=300, placeholder_text="Año (e.g., 2021)")
        self.wine_year_entry.pack(pady=10)

        # Campo para ingresar la descripción del vino
        self.wine_description_entry = ctk.CTkEntry(self.add_review_frame, width=300, placeholder_text="Descripción (e.g., crujiente con toques de roble)")
        self.wine_description_entry.pack(pady=10)

        self.confirm_button = ctk.CTkButton(
            self.add_review_frame,
            text="Confirmar",
            command=self.save_review
        )
        self.confirm_button.pack(pady=10)

        # Detectar cuando se hace clic fuera del frame flotante para cerrarlo
        self.root.bind("<Button-1>", self.hide_review_frame)
    
    def hide_review_frame(self, event):
        """ Oculta el frame flotante si se hace clic fuera de él """
        if hasattr(self, 'add_review_frame') and self.add_review_frame.winfo_ismapped():
            if not (self.add_review_frame.winfo_rootx() <= event.x_root <= self.add_review_frame.winfo_rootx() + self.add_review_frame.winfo_width() and
                    self.add_review_frame.winfo_rooty() <= event.y_root <= self.add_review_frame.winfo_rooty() + self.add_review_frame.winfo_height()):
                self.add_review_frame.place_forget()  # Ocultar el frame
                self.root.unbind("<Button-1>")
    def save_review(self):
        """ Guardar una nueva reseña y actualizar el archivo JSON """
        wine_name = self.wine_name_entry.get()
        wine_year = self.wine_year_entry.get()
        wine_description = self.wine_description_entry.get()

        if wine_name and wine_year and wine_description:
            new_review = {
                "wine_name": wine_name,
                "year": wine_year,
                "review_text": wine_description
            }

            # Cargar reseñas existentes, si el archivo existe
            if os.path.exists('data/reviews.json'):
                with open('data/reviews.json', 'r') as file:
                    reviews = json.load(file)  # Cargar reseñas existentes
            else:
                reviews = []  # Inicializar lista si no existe el archivo

            # Agregar la nueva reseña
            reviews.append(new_review)

            # Guardar todo de nuevo en el archivo JSON
            self.save_reviews(reviews)

            # Actualizar las reseñas mostradas
            self.load_reviews()  # Agregar esta línea
            self.add_review_frame.place_forget()
            

    def save_reviews(self, reviews):
        """ Guardar las reseñas en un archivo JSON """
        with open('data/reviews.json', 'w') as file:
            json.dump(reviews, file, indent=4)
 
 
#Ver mas Review
    def show_all_reviews_frame(self):
        """ Muestra todas las reseñas en un frame flotante """
        all_reviews_frame = ctk.CTkFrame(self.root, fg_color=self.colors["DARK_BURGUNDY"])
        all_reviews_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.8)

        with open('data/reviews.json', 'r') as f:
            reviews = json.load(f)

        for review in reviews:
            review_box = ctk.CTkTextbox(
                all_reviews_frame,
                height=40,
                font=("Helvetica", 12),
                fg_color=self.colors["cream"],
                text_color=self.colors["DARK_BURGUNDY"],
            )
            review_box.insert(ctk.END, f"{review['wine_name']} ({review['year']})\n{review['review_text']}")
            review_box.pack(fill="x", pady=2)

        # Detectar clic fuera del frame para cerrarlo
        self.root.bind("<Button-1>", lambda event: self.close_frame_on_click(event, all_reviews_frame))

    def close_frame_on_click(self, event, frame):
        """ Cerrar el frame si se hace clic fuera de él """
        widget = event.widget
        if widget not in frame.winfo_children() and widget != frame:
            frame.place_forget() 
    
    def photo_main(self,frame_main):
        # Profile Photo
        self.photo_frame = ctk.CTkFrame(
            frame_main,
            width=150,
            height=150,
            corner_radius=75,  # Ensures the frame is circular
            fg_color=self.colors["DARK_BURGUNDY"],
        )
        self.photo_frame.place(relx=0.5, rely=0.2, anchor="center")

        self.canvas = ctk.CTkCanvas(
            self.photo_frame,
            width=150,
            height=150,
            bg=self.colors["DARK_BURGUNDY"],
            highlightthickness=0,
        )
        self.canvas.pack(fill="both", expand=True)

        # Cargar la imagen predeterminada
        self.load_default_photo()

        # Load profile photo button
        self.load_photo_button = ctk.CTkButton(
            frame_main,
            text="Cargar Imagen",
            command=self.load_photo,
            fg_color=self.colors["LIGHT_BURGUNDY"],
            hover_color=self.colors["gold"],
        )
        self.load_photo_button.place(relx=0.5, rely=0.35, anchor="center")
        
    
#Mostrar Ventanas
    def show_favs(self):
        self.main_frame.pack_forget()
        self.comp = FavtsPrograma(self.root,self.show_main_window)

    def show_perfil(self):
        self.main_frame.pack_forget()
        self.comp = Perfil_Programa(self.root, self.show_main_window, user_data)

    def show_main_window(self,frame_favts):
        frame_favts.pack_forget()
        self.create_widgets()
        self.layout_widgets()
        self.root.after(100, self.load_reviews)
#Cambiar todo en una sola ventana, en el mismo Frame principal

    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    user_data = {
    "name": "Ramiro",  
    "bio": "Me encanta el vino tinto y tengo una colección de vinos internacionales.",
    "fav_wine": "Malbec",
}
    app = WineAppMobileGUI(user=user_data)
    app.root.mainloop()

