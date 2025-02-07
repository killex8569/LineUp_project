import customtkinter as ctk

class Playlist(ctk.CTkFrame):
    def __init__(self, master, playlists, **kwargs):
        super().__init__(master, **kwargs)
