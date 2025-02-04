import customtkinter
from PIL import Image

class Layout(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Frame 1
        self.logo_png = customtkinter.CTkImage(Image.open("data/LineUp.png"), size=(100, 100))
        self.logo = customtkinter.CTkLabel(master=self, image=self.logo_png, text="", fg_color="#4A90E2")
        self.logo.grid(row=0, column=0)
        # frame 2
        self.frame = customtkinter.CTkFrame(master=self, fg_color="#4A90E2", corner_radius=0)
        self.frame.grid(row=1, column=0, sticky="nswe")
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        
        self.setting_png = customtkinter.CTkImage(Image.open("data/setting.png"), size=(20, 20))
        self.account_png = customtkinter.CTkImage(Image.open("data/account.png"), size=(20, 20))
        self.playlist_png = customtkinter.CTkImage(Image.open("data/playlist.png"), size=(20, 20))
        self.download_png = customtkinter.CTkImage(Image.open("data/download-circular-button.png"), size=(20, 20))
        self.youtube_png = customtkinter.CTkImage(Image.open("data/youtube.png"), size=(20, 20))
        
        self.btn_youtube = customtkinter.CTkButton(master=self.frame, text="Youtube", width=150, height=50, text_color="white", fg_color="transparent", image=self.youtube_png)
        self.btn_youtube.grid(row=1, column=1, pady=25, padx=40)
        self.btn_url_download = customtkinter.CTkButton(master=self.frame, text="Download", width=150, height=50, text_color="white", fg_color="transparent", image=self.download_png)
        self.btn_url_download.grid(row=2, column=1, pady=25, padx=40)
        self.btn_playlist = customtkinter.CTkButton(master=self.frame, text="Playlist", width=150, height=50, text_color="white", fg_color="transparent", image=self.playlist_png)
        self.btn_playlist.grid(row=3, column=1, pady=25, padx=40)
        self.btn_account = customtkinter.CTkButton(master=self.frame, text="Account", width=150, height=50, text_color="white", fg_color="transparent", image=self.account_png)
        self.btn_account.grid(row=5, column=1, pady=25, padx=40)
        self.btn_setting = customtkinter.CTkButton(master=self.frame, text="Setting", width=150, height=50, text_color="white", fg_color="transparent", image=self.setting_png)
        self.btn_setting.grid(row=4, column=1, pady=25, padx=40)