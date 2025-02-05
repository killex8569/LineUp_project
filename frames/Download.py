import customtkinter

class Download(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.label_download = customtkinter.CTkLabel(master=self, text="Download section", font=("Arial", 16))
        self.label_download.grid(padx=10, pady=10)
        
        self.download_btn = customtkinter.CTkButton(master=self, text="download vidéo")
        self.download_btn.grid(row=1, column=1, padx=10, pady=10)
        
        self.download_entry = customtkinter.CTkEntry(master=self, placeholder_text="votre url youtube")
        self.download_entry.grid(row=1, column=0, padx=10, pady=10)
