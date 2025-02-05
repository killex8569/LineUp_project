import customtkinter

class Setting(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.label_theme = customtkinter.CTkLabel(master=self, text="theme setting")
        self.label_theme.grid()
        
# theme color
        self.theme_options = ["Dark", "Light", "System"]

        # Création du menu déroulant
        self.theme_menu = customtkinter.CTkOptionMenu(
            self,
            values=self.theme_options,
            command=self.change_theme
        )
        self.theme_menu.grid(pady=20, padx=20)

    def change_theme(self, selected_theme):
        if selected_theme == "Dark":
            customtkinter.set_appearance_mode("dark")
            
        elif selected_theme == "Light":
            customtkinter.set_appearance_mode("light")
        else:
            customtkinter.set_appearance_mode("system")