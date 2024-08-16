import customtkinter as ctk
from PIL import Image, ImageTk

class WineAppMobileGUI:
    def __init__(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")

        self.root = ctk.CTk()
        self.root.title("Wine Enthusiast Profile")
        self.root.geometry("360x640")  # Common Android phone resolution

        # Color palette inspired by wine
        self.colors = {
            "burgundy": "#800020",
            "wine_red": "#722F37",
            "cream": "#F2E8CF",
            "cork": "#C3A98A",
            "bottle_green": "#2C5E4C"
        }

        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        # Profile Photo
        self.photo_frame = ctk.CTkFrame(self.root, width=120, height=120, corner_radius=60, fg_color=self.colors["cork"])
        self.photo_label = ctk.CTkLabel(self.photo_frame, text="", fg_color=self.colors["cream"])
        self.photo_label.pack(expand=True, fill="both", padx=5, pady=5)

        # Name
        self.name_entry = ctk.CTkEntry(self.root, placeholder_text="Your Name", 
                                       font=("Helvetica", 18), width=250, 
                                       fg_color=self.colors["cream"], text_color=self.colors["wine_red"])

        # Favorite Wine
        self.fav_wine_entry = ctk.CTkEntry(self.root, placeholder_text="Favorite Wine", 
                                           font=("Helvetica", 14), width=250, 
                                           fg_color=self.colors["cream"], text_color=self.colors["wine_red"])

        # About
        self.about_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.about_label = ctk.CTkLabel(self.about_frame, text="About Me", 
                                        font=("Helvetica", 16, "bold"), text_color=self.colors["burgundy"])
        self.about_text = ctk.CTkTextbox(self.about_frame, wrap="word", height=80, 
                                         font=("Helvetica", 14), width=300, 
                                         fg_color=self.colors["cream"], text_color=self.colors["wine_red"])
        self.about_text.insert("1.0", "Share your passion for wine...")

        # Last Reviews
        self.reviews_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.reviews_label = ctk.CTkLabel(self.reviews_frame, text="Recent Wine Reviews", 
                                          font=("Helvetica", 16, "bold"), text_color=self.colors["burgundy"])
        self.review1 = ctk.CTkLabel(self.reviews_frame, text="2022 Cabernet Sauvignon - Rich and full-bodied", 
                                    font=("Helvetica", 14), fg_color=self.colors["cream"], 
                                    corner_radius=8, pady=5)
        self.review2 = ctk.CTkLabel(self.reviews_frame, text="2021 Chardonnay - Crisp with hints of oak", 
                                    font=("Helvetica", 14), fg_color=self.colors["cream"], 
                                    corner_radius=8, pady=5)

        # Buttons
        self.button_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.add_review_button = ctk.CTkButton(self.button_frame, text="Add Review", 
                                               fg_color=self.colors["bottle_green"], 
                                               hover_color=self.colors["wine_red"])
        self.edit_profile_button = ctk.CTkButton(self.button_frame, text="Edit Profile", 
                                                 fg_color=self.colors["burgundy"], 
                                                 hover_color=self.colors["wine_red"])

    def layout_widgets(self):
        self.root.configure(fg_color=self.colors["cork"])
        
        self.photo_frame.pack(pady=(30, 15))
        self.name_entry.pack(pady=10)
        self.fav_wine_entry.pack(pady=10)

        self.about_frame.pack(pady=10, padx=20, fill="x")
        self.about_label.pack(anchor="w")
        self.about_text.pack(fill="x", pady=5)

        self.reviews_frame.pack(pady=10, padx=20, fill="x")
        self.reviews_label.pack(anchor="w", pady=(0, 5))
        self.review1.pack(fill="x", pady=2)
        self.review2.pack(fill="x", pady=2)

        self.button_frame.pack(side="bottom", fill="x", padx=20, pady=20)
        self.add_review_button.pack(side="left", expand=True, padx=5)
        self.edit_profile_button.pack(side="right", expand=True, padx=5)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = WineAppMobileGUI()
    app.run()
