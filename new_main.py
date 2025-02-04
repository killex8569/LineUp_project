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
        self.iconbitmap("data\\LineUp.ico")
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        
        # main frame
        self.frame = ctk.CTkFrame(master=self, fg_color="#4A90E2", corner_radius=0)
        self.frame.grid(row=1, column=0, sticky="nsw")
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        
        # startup frame
        self.startup_frame = Youtube(master=self, corner_radius=10)
        self.startup_frame.grid(row=1, column=1, sticky="nsw")
        self.grid_columnconfigure(1, weight=99)
        
        # paramètres
        self.logo_png = ctk.CTkImage(Image.open("data/LineUp.png"), size=(100, 100))
        self.logo = ctk.CTkLabel(master=self.frame, image=self.logo_png, text="", fg_color="#4A90E2")
        self.logo.grid(row=0, column=1)
        
        self.setting_png = ctk.CTkImage(Image.open("data/setting.png"), size=(20, 20))
        self.account_png = ctk.CTkImage(Image.open("data/account.png"), size=(20, 20))
        self.playlist_png = ctk.CTkImage(Image.open("data/playlist.png"), size=(20, 20))
        self.download_png = ctk.CTkImage(Image.open("data/download-circular-button.png"), size=(20, 20))
        self.youtube_png = ctk.CTkImage(Image.open("data/youtube.png"), size=(20, 20))
        
        self.btn_youtube = ctk.CTkButton(master=self.frame, text="Youtube", width=150, height=50, text_color="white", fg_color="transparent", image=self.youtube_png)
        self.btn_youtube.grid(row=1, column=1, pady=25, padx=40)
        self.btn_url_download = ctk.CTkButton(master=self.frame, text="Download", width=150, height=50, text_color="white", fg_color="transparent", image=self.download_png)
        self.btn_url_download.grid(row=2, column=1, pady=25, padx=40)
        self.btn_playlist = ctk.CTkButton(master=self.frame, text="Playlist", width=150, height=50, text_color="white", fg_color="transparent", image=self.playlist_png)
        self.btn_playlist.grid(row=3, column=1, pady=25, padx=40)
        self.btn_account = ctk.CTkButton(master=self.frame, text="Account", width=150, height=50, text_color="white", fg_color="transparent", image=self.account_png)
        self.btn_account.grid(row=5, column=1, pady=25, padx=40)
        self.btn_setting = ctk.CTkButton(master=self.frame, text="Setting", width=150, height=50, text_color="white", fg_color="transparent", image=self.setting_png)
        self.btn_setting.grid(row=4, column=1, pady=25, padx=40)
        
    def change_frame(self, new_frame):
        self.startup_frame.grid_forget()
        self.startup_frame = new_frame
    



lineup = Lineup()
lineup.mainloop()