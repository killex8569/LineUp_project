import os
import tkinter
import customtkinter
from customtkinter import *

# set the default appearance
customtkinter.set_appearance_mode("dark")

# deactivate automatic scaling
customtkinter.deactivate_automatic_dpi_awareness()

# ajout de l'interface
lineup = CTk()
lineup.geometry("600x500")

login_frame = customtkinter.CTkFrame(master=lineup)
login_frame.pack(pady=50, padx=50)


login_button = customtkinter.CTkButton(master=login_frame, text="connexion")
login_button.pack(pady=12, padx=10)


lineup.mainloop()