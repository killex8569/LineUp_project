import customtkinter

class Account(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.section_passwd = customtkinter.CTkLabel(master=self, text="Password Section", font=("Arial", 16))
        self.section_passwd.grid(row=0, column=2, sticky="nswe", padx=5, pady=5)
        
        self.current_passwd_entry = customtkinter.CTkEntry(master=self, corner_radius=5, placeholder_text="mot de passe actuelle")
        self.current_passwd_entry.grid(row=1, column=2, sticky="nswe", padx=5, pady=5)
        
        self.new_passwd_entry = customtkinter.CTkEntry(master=self, corner_radius=5, placeholder_text="Nouveau mot de passes")
        self.new_passwd_entry.grid(row=1, column=3, sticky="nswe", padx=5, pady=5)
        
        self.account_btn_change_passwd = customtkinter.CTkButton(master=self, corner_radius=5, text="sauvegarder")
        self.account_btn_change_passwd.grid(row=1, column=4, sticky="nswe", padx=5, pady=5)
        
        self.change_account_label = customtkinter.CTkLabel(master=self, text="login")
        self.change_account_label.grid(row=3, column=2, sticky="nswe", padx=5, pady=5)
        
        self.account_change_user_btn = customtkinter.CTkButton(master=self, text="Deconnexion")
        self.account_change_user_btn.grid(row=4, column=2, sticky="nswe", padx=5, pady=5)






