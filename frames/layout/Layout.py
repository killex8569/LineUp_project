import customtkinter
from PIL import Image
from frames.Youtube import Youtube
from frames.Download import Download
from frames.Playlist import Playlist
from frames.Setting import Setting
from frames.Account import Account
from frames.Login import Login
from frames.info_dev import Info_Dev

from db.daos.DAOPlaylist import DAOPlaylist

class Layout(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # frame 1
        self.frame = customtkinter.CTkFrame(master=self, fg_color="#4A90E2", corner_radius=0)
        self.frame.grid(row=1, column=0, sticky="nswe")
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        
        # paramètres
        self.logo_png = customtkinter.CTkImage(Image.open("data/LineUp.png"), size=(100, 100))
        self.logo = customtkinter.CTkLabel(master=self.frame, image=self.logo_png, text="", fg_color="#4A90E2")
        self.logo.grid(row=0, column=1)
        
        self.setting_png = customtkinter.CTkImage(Image.open("data/setting.png"), size=(20, 20))
        self.account_png = customtkinter.CTkImage(Image.open("data/account.png"), size=(20, 20))
        self.playlist_png = customtkinter.CTkImage(Image.open("data/playlist.png"), size=(20, 20))
        self.download_png = customtkinter.CTkImage(Image.open("data/download-circular-button.png"), size=(20, 20))
        self.youtube_png = customtkinter.CTkImage(Image.open("data/youtube.png"), size=(20, 20))
        self.logs_png = customtkinter.CTkImage(Image.open("data/logs.png"), size=(20, 20))

        self.btn_youtube = customtkinter.CTkButton(master=self.frame, text="Youtube", width=150, height=50, text_color="white", fg_color="transparent", image=self.youtube_png, command=self.getYoutubePage)
        self.btn_youtube.grid(row=1, column=1, pady=20, padx=30)
        self.btn_url_download = customtkinter.CTkButton(master=self.frame, text="Download", width=150, height=50, text_color="white", fg_color="transparent", image=self.download_png, command=self.getDownloadPage)
        self.btn_url_download.grid(row=2, column=1, pady=20, padx=30)
        self.btn_playlist = customtkinter.CTkButton(master=self.frame, text="Playlist", width=150, height=50, text_color="white", fg_color="transparent", image=self.playlist_png, command=self.getPlaylistPage)
        self.btn_playlist.grid(row=3, column=1, pady=20, padx=30)
        self.btn_setting = customtkinter.CTkButton(master=self.frame, text="Setting", width=150, height=50, text_color="white", fg_color="transparent", image=self.setting_png, command=self.getSettingPage)
        self.btn_setting.grid(row=4, column=1, pady=20, padx=30)
        self.btn_account = customtkinter.CTkButton(master=self.frame, text="Account", width=150, height=50, text_color="white", fg_color="transparent", image=self.account_png, command=self.getAccountPage)
        self.btn_account.grid(row=5, column=1, pady=5, padx=0)
        self.account_btn_info_dev = customtkinter.CTkButton(master=self.frame, text="Releases", width=150, height=50, text_color="white", fg_color="transparent", image=self.logs_png, command=self.getInfoDevPage)
        self.account_btn_info_dev.grid(row=6, column=1, sticky="nswe", pady=20, padx=30)
    
    def getYoutubePage(self):
        self.master.change_frame(Youtube(master=self))

    def getPlaylistPage(self):
        dao = DAOPlaylist('db/database.json')
        DBplaylists = dao.getAll()
        self.master.change_frame(Playlist(master=self, playlists=DBplaylists))
    
    def getDownloadPage(self):
        self.master.change_frame(Download(master=self))

    def getSettingPage(self):
        self.master.change_frame(Setting(master=self))
    
    def getAccountPage(self):
        self.master.change_frame(Account(master=self))
        
    def getloginPage(self):
        self.master.change_frame(Login(master=self))
    
    def getInfoDevPage(self):
        self.master.change_frame(Info_Dev(master=self))
    

    