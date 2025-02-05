import customtkinter

class Info_Dev(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(master=self, text="dev logs")
        self.label.grid()
        