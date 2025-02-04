import customtkinter
from customtkinter import CTk
from PIL import Image

class Youtube(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.youtube_frame = customtkinter.CTkFrame(master=self, fg_color="#4A90E2", corner_radius=0)
        self.youtube_frame.grid(row=0, column=1, rowspan=5, columnspan=5, sticky="nswe", padx=0, pady=0)
        
        self.youtube_entry = customtkinter.CTkEntry(master=self, corner_radius=0, placeholder_text="Recherche sur Youtube")
        self.youtube_entry.grid(row=0, column=1, rowspan=5, columnspan=5, sticky="nswe", padx=0, pady=0)
        
        self.youtube_btn = customtkinter.CTkButton(master=self, corner_radius=0, text="Recherche")
        self.youtube_btn.grid(row= 1, column=2, padx=5, pady=5)
