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
        
        self.layoutmain = LayoutMain(master=self)
        self.layoutmain.grid()
    

class LayoutMain(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.frame = ctk.CTkFrame(master=self)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        self.contentFrame = Layout(master=self)
        self.contentFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
    
    
    def change_frame(self, newFrame):
        self.current_frame = newFrame
            
        

lineup = Lineup()
lineup.mainloop()