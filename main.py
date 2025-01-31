import os
import tkinter
import customtkinter
from customtkinter import *
from tkinter import PhotoImage
from PIL import Image
from PyInstaller import *

# set the default appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# deactivate automatic scaling
customtkinter.deactivate_automatic_dpi_awareness()

# ajout de l'interface
lineup = CTk()
lineup.geometry("600x500")
lineup.title("LineUp")
lineup.iconbitmap("data/LineUp.ico")

# Création de la frame (logo)
content_frame = customtkinter.CTkFrame(master=lineup, fg_color="#1E90FF", corner_radius=0)
content_frame.grid(row=0, column=0, sticky="nswe")
content_frame.grid_columnconfigure(1, weight=1)
content_frame.grid_rowconfigure(0, weight=1)

# Contenue de la frame logo
logo_png = customtkinter.CTkImage(light_image=Image.open("data/LineUp.png"))
logo = customtkinter.CTkLabel(master=content_frame, image=logo_png)
logo.grid()


# Création de la frame 2 (action)
content_frame2 = customtkinter.CTkFrame(master=lineup, fg_color="#1E90FF", corner_radius=0)
content_frame2.grid(row=1, column=0, sticky="nswe")
content_frame2.grid_columnconfigure(1, weight=1)
content_frame2.grid_rowconfigure(1, weight=1)

# Création de la frame 3 (account)
content_frame3 = customtkinter.CTkFrame(master=lineup, fg_color="#1E90FF", corner_radius=0)
content_frame3.grid(row=2, column=0, sticky="nswe")
content_frame3.grid_columnconfigure(1, weight=1)
content_frame3.grid_rowconfigure(2, weight=1)


# Création de la frame 4 (end)
content_frame4 = customtkinter.CTkFrame(master=lineup, fg_color="#1E90FF", corner_radius=0)
content_frame4.grid(row=3, column=0, sticky="nswe")
content_frame4.grid_columnconfigure(1, weight=1)
content_frame4.grid_rowconfigure(2, weight=1)


lineup.mainloop()