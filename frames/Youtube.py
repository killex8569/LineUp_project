import customtkinter
from customtkinter import CTk
from PIL import Image


class Youtube(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.youtube_label = customtkinter.CTkLabel(master=self, text="résultat recherche youtube", font=("Arial", 16))
        self.youtube_label.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)

        self.youtube_entry = customtkinter.CTkEntry(master=self, corner_radius=5, placeholder_text="Recherche sur Youtube")
        self.youtube_entry.grid(row=2, column=1, sticky="nswe", padx=10, pady=10)
        
        self.youtube_btn = customtkinter.CTkButton(master=self, corner_radius=5, text="Recherche")
        self.youtube_btn.grid(row=2, column=2, sticky="nswe", padx=10, pady=10)
        


