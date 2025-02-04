import customtkinter
from customtkinter import CTk
from PIL import Image

class youtube(CTk):
    def __init__(self):
        super().__init__()
        self.youtube_frame = customtkinter.CTkFrame(master=self, fg_color="#4A90E2", corner_radius=0)
        self.youtube_frame.grid()
    