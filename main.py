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

def settings():
    print("Bienvenue dans les settings")
    # masque les frames :
    navbar_frame.grid_forget()
    account_frame.grid_forget()
    download_frame.grid_forget()
    playlist_frame.grid_forget()

    # afficher les frames :
    setting_lineup.grid(row=0, column=1, rowspan=5, columnspan=5, sticky="nswe")

def account():
    print("Bienvenue dans le compte")
    # masquer les frames :
    navbar_frame.grid_forget()
    setting_lineup.grid_forget()
    download_frame.grid_forget()
    playlist_frame.grid_forget()

    # afficher les frames :
    account_frame.grid(row=0, column=1, rowspan=5, columnspan=5, sticky="nswe")

def youtube():
    print("Bienvenue dans youtube")
    # masquer les frames
    account_frame.grid_forget()
    setting_lineup.grid_forget()
    download_frame.grid_forget()
    playlist_frame.grid_forget()

    # afficher les frames
    navbar_frame.grid(row=0, column=1, rowspan=5, columnspan=5, sticky="nswe")

def playlist():
    print("Bienvenue dans vos playlist")
    account_frame.grid_forget()
    setting_lineup.grid_forget()
    download_frame.grid_forget()
    navbar_frame.grid_forget()
    
    playlist_frame.grid(row=0, column=1, rowspan=5, columnspan=5, sticky="nswe")

def download():
    print("Bienvenue dans vos téléchargement")
    account_frame.grid_forget()
    setting_lineup.grid_forget()
    navbar_frame.grid_forget()
    playlist_frame.grid_forget()
    
    download_frame.grid(row=0, column=1, rowspan=5, columnspan=5, sticky="nswe")
        
def new_credentials():
    print("Bienvenue dans le gestionnaire de changement de mot de passe ! ")
    

def login():
    login = "admin"
    password = "123456"
    
    entry_login = login_entry.get()
    entry_passwd = passwd_entry.get()
    if entry_login == login and entry_passwd == password:
        login_frame.grid_forget()
        content_frame.grid(row=0, column=0, sticky="nswe")
        content_frame2.grid(row=1, column=0, sticky="nswe")
        navbar_frame.grid(row=0, column=1, rowspan=5, columnspan=5, sticky="nswe", padx=0, pady=0)
    else:
        print("invalid credentials")


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
btn_youtube = customtkinter.CTkButton(master=content_frame2, text="Youtube", width=150, height=50, text_color="white", font=lineup_font, fg_color="transparent", image=youtube_png, command=youtube)
btn_youtube.grid(row=1, column=1, pady=25, padx=40)
btn_url_download = customtkinter.CTkButton(master=content_frame2, text="Download", width=150, height=50, text_color="white", font=lineup_font, fg_color="transparent", image=download_png, command=download)
btn_url_download.grid(row=2, column=1, pady=25, padx=40)
btn_playlist = customtkinter.CTkButton(master=content_frame2, text="Playlist", width=150, height=50, text_color="white", font=lineup_font, fg_color="transparent", image=playlist_png, command=playlist)
btn_playlist.grid(row=3, column=1, pady=25, padx=40)
btn_account = customtkinter.CTkButton(master=content_frame2, text="Account", width=150, height=50, text_color="white", font=lineup_font, fg_color="transparent", image=account_png, command=account)
btn_account.grid(row=5, column=1, pady=25, padx=40)
btn_setting = customtkinter.CTkButton(master=content_frame2, text="Setting", width=150, height=50, text_color="white", font=lineup_font, fg_color="transparent", image=setting_png, command=settings)
btn_setting.grid(row=4, column=1, pady=25, padx=40)

# navbar
navbar_frame = customtkinter.CTkFrame(master=lineup, corner_radius=0)
navbar_frame.grid(row=0, column=1, rowspan=5, columnspan=5, sticky="nswe", padx=0, pady=0)

# Contenu principal (NAVBAR FRAME)
navbar_entry_youtube = customtkinter.CTkEntry(master=navbar_frame, placeholder_text="Recherche sur Youtube")
navbar_entry_youtube.grid(row=1, column=1, padx=5)

# button navbar frame
navbar_btn = customtkinter.CTkButton(master=navbar_frame, text="recherche", command=youtube_recherche)
navbar_btn.grid(row= 1, column=2, padx=5, pady=5)

# setting frame
setting_lineup = customtkinter.CTkFrame(master=lineup)
setting_lineup.grid(row=0, column=1, rowspan=5, columnspan=5, sticky="nswe", padx=0, pady=0)

# Button setting frame


# Download frame
download_frame = customtkinter.CTkFrame(master=lineup)
download_frame.grid(row=0, column=1, rowspan=5, columnspan=5, sticky="nswe", padx=0, pady=0)

# Button Download frame

# account frame
account_frame = customtkinter.CTkFrame(master=lineup)
account_frame.grid(row=0, column=1, rowspan=5, columnspan=5, sticky="nswe", padx=0, pady=0)

# Action account frame
account_label = customtkinter.CTkLabel(master=account_frame, text="Credentials", font=("Arial", 16))
account_label.grid(row=6, column=1, sticky="nswe", padx=10, pady=10)

account_entry_modify_login = customtkinter.CTkEntry(master=account_frame, placeholder_text="actual password")
account_entry_modify_login.grid(row=7, column=1, sticky="nswe", padx=8, pady=8)

account_entry_modify_password = customtkinter.CTkEntry(master=account_frame, placeholder_text="New password")
account_entry_modify_password.grid(row=7, column=2, sticky="nswe", padx=8, pady=8)

account_btn_modify_credential = customtkinter.CTkButton(master=account_frame, corner_radius=5, text="change Credentials", command=new_credentials)
account_btn_modify_credential.grid(row=7, column=3, sticky="nswe", padx=8, pady=8)


# Playlist frame
playlist_frame = customtkinter.CTkLabel(master=lineup, text="")
playlist_frame.grid(row=0, column=1, rowspan=5, columnspan=5, sticky="nswe", padx=0, pady=0)


# Initialisation : Masquer les frames autres que la navbar au départ
setting_lineup.grid_forget()
account_frame.grid_forget()
playlist_frame.grid_forget()
download_frame.grid_forget()
navbar_frame.grid_forget()
content_frame.grid_forget()
content_frame2.grid_forget()


# login frame

login_frame = customtkinter.CTkFrame(master=lineup)
login_frame.grid(row=1, column=3, sticky="nswe", padx=10, pady=10)

# Login Button

login_entry = customtkinter.CTkEntry(master=login_frame, placeholder_text="votre login")
login_entry.grid(row=0, column=0, padx=10, pady=10)

passwd_entry = customtkinter.CTkEntry(master=login_frame, placeholder_text="votre mot de passe", show="*")
passwd_entry.grid(row=1, column=0, padx=10, pady=10)

login_btn = customtkinter.CTkButton(master=login_frame, text="connexion", command=login)
login_btn.grid(row=2, column=0, padx=10, pady=10)

# Lancement de la boucle
lineup.mainloop()
