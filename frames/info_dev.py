import customtkinter

class Info_Dev(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(master=self, text="dev logs", font=("Arial", 16))
        self.label.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)

        self.textBox = customtkinter.CTkTextbox(master=self)
        self.textBox.grid(row=2, column=1, columnspan=5, sticky="nswe", padx=10, pady=10)
        
        self.textBox_2 = customtkinter.CTkTextbox(master=self)
        self.textBox_2.grid(row=3, column=1, columnspan=5, sticky="nswe", padx=10, pady=10)

        self.textBox.insert("0.0", "Nouveauté : \n\n1 - Utilisation de la POO comme base\n2 - Ajout de pages (Account etc... settings)")
        self.textBox_2.insert("0.0", "Futures mise à jours : \n\n- Mise en place de playlist avec un CRUD pour les musiques")
        