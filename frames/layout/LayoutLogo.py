import customtkinter
from PIL import Image

class LayoutLogo(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Frame 1
        self.content_frame = customtkinter.CTkFrame(master=self, fg_color="#4A90E2", corner_radius=0)
        self.content_frame.grid(row=0, column=0, sticky="nswe")
        self.content_frame.grid_columnconfigure(1, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)
        
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.logo_png = customtkinter.CTkImage(Image.open("data/LineUp.png"), size=(100, 100))
        self.logo = customtkinter.CTkLabel(master=self, image=self.logo_png, text="", fg_color="#4A90E2")
        self.logo.grid(row=0, column=0)