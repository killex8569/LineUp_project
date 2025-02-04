import customtkinter as ctk

class Playlist(ctk.CTkFrame):
    def __init__(self, master, playlists,**kwargs):
        super().__init__(master, **kwargs)
        
        self.playlists = playlists
        self.textbox = ctk.CTkTextbox(master)
        self.textbox.grid(row=0, column=0, sticky="nsew")

        for playlist in self.playlists:
            self.textbox.insert("0.0", playlist.libelle)
