import customtkinter
from customtkinter import CTk
from PIL import Image


class Youtube(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.youtube_entry = customtkinter.CTkEntry(master=self, corner_radius=5, placeholder_text="Recherche sur Youtube")
        self.youtube_entry.grid(row=0, column=2, sticky="nswe", padx=5, pady=5)
        
        self.youtube_btn = customtkinter.CTkButton(master=self, corner_radius=5, text="Recherche")
        self.youtube_btn.grid(row=0, column=3, sticky="nswe", padx=5, pady=5)
        
        self.youtube_label = customtkinter.CTkLabel(master=self, text="résultat recherche youtube")
        self.youtube_label.grid(row=1, column=2, sticky="nswe", padx=5, pady=5)

