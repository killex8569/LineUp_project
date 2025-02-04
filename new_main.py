import customtkinter as ctk
import PIL
from PIL import Image

from frames.layout.LayoutLogo import LayoutLogo
from frames.layout.LayoutMenu import LayoutMenu


class Lineup(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x600")
        self.title("LineUp")
        self.iconbitmap("data/LineUp.ico")
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        
        self.layoutMain = ctk.CTkFrame(master=self)
        self.layoutMain.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        self.contentFrame = LayoutLogo(master=self.layoutMain)
        self.contentFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        self.frame = LayoutMenu(master=self.layoutMain)
        self.frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")


lineup = Lineup()
lineup.mainloop()