import customtkinter as ctk
import PIL
from PIL import Image

from frames.layout.Layout import Layout
from frames.Youtube import Youtube
from frames.Account import Account



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

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
        self.layoutmain.grid(row=0, column=0, sticky="nsw")
        
        self.current_frame = Youtube(master=self)
        self.current_frame.grid(row=0, column=0)
        
    def change_frame(self, new_frame):
        self.current_frame = new_frame



lineup = Lineup()
lineup.mainloop()