import customtkinter as ctk
import PIL
from PIL import Image

from frames.layout.Layout import Layout
from frames.youtube import youtube


class Lineup(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x600")
        self.title("LineUp")
        self.iconbitmap("data/LineUp.ico")
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        
        self.layoutmain = Layout(master=self)
        self.layoutmain.grid()
        

lineup = Lineup()
lineup.mainloop()