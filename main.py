# fait par deux étudiant Français
# Make by Killex8569 and ValentinRyckaert
import os
import tkinter
import customtkinter
from customtkinter import *
from tkinter import PhotoImage
from PIL import Image
from PyInstaller import *
from tkinter import font
import tkinter.font as tkFont
from pytube import *

# set the default appearance and font
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Deactivate automatic scaling
customtkinter.deactivate_automatic_dpi_awareness()

# Research function
def youtube_recherche():
    url_ytb = navbar_entry_youtube.get()
    print("votre recherche est : ", url_ytb)
    

# Add interface
lineup = CTk()
lineup.geometry("700x600")
lineup.title("LineUp")
lineup.iconbitmap("data/LineUp.ico")
lineup.resizable(False, False)

# Add font
font_path = "/data/Kanit/Kanit-Regular.ttf"
lineup_font = customtkinter.CTkFont(family="Kanit", size=16)
lineup.option_add("*font", lineup_font)


# Create frame (logo)
content_frame = customtkinter.CTkFrame(master=lineup, fg_color="#1E90FF", corner_radius=0)
content_frame.grid(row=0, column=0, sticky="nswe")
content_frame.grid_columnconfigure(1, weight=1)
content_frame.grid_rowconfigure(0, weight=1)

# Content frame logo
content_frame.grid_columnconfigure(0, weight=1)
content_frame.grid_rowconfigure(0, weight=1)
logo_png = customtkinter.CTkImage(Image.open("data/LineUp.png"), size=(100, 100))
logo = customtkinter.CTkLabel(master=content_frame, image=logo_png, text="", padx=40)
logo.grid(row=0, column=0)

# Create frame 2 (action)
content_frame2 = customtkinter.CTkFrame(master=lineup, fg_color="#1E90FF", corner_radius=0)
content_frame2.grid(row=1, column=0, sticky="nswe")
content_frame2.grid_columnconfigure(1, weight=1)
content_frame2.grid_rowconfigure(1, weight=1)

# img for button
setting_png = customtkinter.CTkImage(Image.open("data/setting.png"), size=(20, 20))
account_png = customtkinter.CTkImage(Image.open("data/account.png"), size=(20, 20))
playlist_png = customtkinter.CTkImage(Image.open("data/playlist.png"), size=(20, 20))
download_png = customtkinter.CTkImage(Image.open("data/download-circular-button.png"), size=(20, 20))
youtube_png = customtkinter.CTkImage(Image.open("data/youtube.png"), size=(20, 20))


# bouton frame 2
btn_youtube = customtkinter.CTkButton(master=content_frame2, text="Youtube", width=150, height=50, text_color="white", font=lineup_font, fg_color="transparent", image=youtube_png)
btn_youtube.grid(row=1, column=1, pady=25, padx=40)
btn_url_download = customtkinter.CTkButton(master=content_frame2, text="URL download", width=150, height=50, text_color="white", font=lineup_font, fg_color="transparent", image=download_png)
btn_url_download.grid(row=2, column=1, pady=25, padx=40)
btn_playlist = customtkinter.CTkButton(master=content_frame2, text="Playlist", width=150, height=50, text_color="white", font=lineup_font, fg_color="transparent", image=playlist_png)
btn_playlist.grid(row=3, column=1, pady=25, padx=40)
btn_account = customtkinter.CTkButton(master=content_frame2, text="Compte", width=150, height=50, text_color="white", font=lineup_font, fg_color="transparent", image=account_png)
btn_account.grid(row=5, column=1, pady=25, padx=40)
btn_setting = customtkinter.CTkButton(master=content_frame2, text="Setting", width=150, height=50, text_color="white", font=lineup_font, fg_color="transparent", image=setting_png)
btn_setting.grid(row=4, column=1, pady=25, padx=40)


# navbar
navbar = customtkinter.CTkFrame(master=lineup, corner_radius=0)
navbar.grid(row=0, column=1, rowspan=5, columnspan=5, sticky="nswe", padx=0, pady=0)


# Contenue principal (NAVBAR FRAME)
navbar_entry_youtube = customtkinter.CTkEntry(master=navbar, placeholder_text="Recherche sur Youtube")
navbar_entry_youtube.grid(row=1, column=1, padx=5)

navbar_btn = customtkinter.CTkButton(master=navbar, text="recherche", command=youtube_recherche)
navbar_btn.grid(row= 1, column=2, padx=5, pady=5)



# button navbar frame


lineup.mainloop()