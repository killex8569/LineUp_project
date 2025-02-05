import customtkinter as ctk

class Playlist(ctk.CTkFrame):
    def __init__(self, master, playlists,**kwargs):
        super().__init__(master, **kwargs)
        
        self.playlists = playlists
        self.textbox = ctk.CTkTextbox(master)
        self.textbox.grid(row=1, column=1, sticky="nsew")
        
        # frame playlist
        self.your_playlist = ctk.CTkScrollableFrame(master)
        self.your_playlist.grid(row=2, column=1, sticky="nsew")
        
        self.create_playlist_btn = ctk.CTkButton(master)
        self.create_playlist_btn.grid(row=3, column=2, sticky="nsew")

        for playlist in self.playlists:
            self.textbox.insert("0.0", playlist.libelle)
