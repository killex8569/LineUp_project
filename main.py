import os
import tkinter
import customtkinter
from customtkinter import *
from tkinter import PhotoImage
from PIL import Image
from PyInstaller import *

# set the default appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# deactivate automatic scaling
customtkinter.deactivate_automatic_dpi_awareness()

# ajout de l'interface
lineup = CTk()
lineup.geometry("700x600")
lineup.title("LineUp")
lineup.iconbitmap("data/LineUp.ico")
lineup.resizable(False, False)


# Création de la frame (logo)
content_frame = customtkinter.CTkFrame(master=lineup, fg_color="#1E90FF", corner_radius=0)
content_frame.grid(row=0, column=0, sticky="nswe")
content_frame.grid_columnconfigure(1, weight=1)
content_frame.grid_rowconfigure(0, weight=1)

# Contenue de la frame logo
content_frame.grid_columnconfigure(0, weight=1)
content_frame.grid_rowconfigure(0, weight=1)
logo_png = customtkinter.CTkImage(Image.open("data/LineUp.png"), size=(100, 100))
logo = customtkinter.CTkLabel(master=content_frame, image=logo_png, text="", padx=40)
logo.grid(row=0, column=0)

# Ajout du label sous le logo
logo_label = customtkinter.CTkLabel(master=content_frame, text="LineUp", font=("Arial", 14), text_color="white")
logo_label.grid(row=1, column=0)

# Création de la frame 2 (action)
content_frame2 = customtkinter.CTkFrame(master=lineup, fg_color="#1E90FF", corner_radius=0)
content_frame2.grid(row=1, column=0, sticky="nswe")
content_frame2.grid_columnconfigure(1, weight=1)
content_frame2.grid_rowconfigure(1, weight=1)

# bouton frame 2
btn_youtube = customtkinter.CTkButton(master=content_frame2, text="Youtube", width=150, height=50)
btn_youtube.grid(row=1, column=1, pady=25, padx=40)
btn_playlist = customtkinter.CTkButton(master=content_frame2, text="Playlist", width=150, height=50)
btn_playlist.grid(row=2, column=1, pady=25, padx=40)
btn_account = customtkinter.CTkButton(master=content_frame2, text="Compte", width=150, height=50)
btn_account.grid(row=3, column=1, pady=25, padx=40)
btn_setting = customtkinter.CTkButton(master=content_frame2, text="setting", width=150, height=50)
btn_setting.grid(row=4, column=1, pady=25, padx=40)


# navbar
navbar = customtkinter.CTkFrame(master=lineup, corner_radius=0)
navbar.grid(row=0, column=1, rowspan=5, columnspan=5, sticky="nswe", padx=0, pady=0)


# Contenue principal (NAVBAR FRAME)
navbar_entry_youtube = customtkinter.CTkEntry(master=navbar, placeholder_text="Recherche sur Youtube")
navbar_entry_youtube.grid(row=1, column=1, padx=5)

navbar_btn = customtkinter.CTkButton(master=navbar, width=150, height=50, text="recherche")
navbar_btn.grid(row= 1, column=2, padx=5, pady=5)



# button navbar frame


lineup.mainloop()