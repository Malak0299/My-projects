from tkinter import *
import customtkinter as c

c.set_appearance_mode("dark")
c.set_default_color_theme("dark-blue")

master = c.CTk()
master.title("Window")
master.geometry("500x500")


label = c.CTkLabel(master, text = "Why is it so dark in here")
label.grid(row = 0, column = 1, padx = 20, pady = 20)

Button = c.CTkButton(master,
                     text = "Navn",
                     height = 50,
                     width = 100,
                     font = ("Helvetica", 24),
                     text_color = "pink",
                     fg_color = "blue",
                     hover_color = "grey",
                     corner_radius = 10,
                     border_width = 1,
                     border_color = "yellow"
                     )
Button.grid (row = 2, column = 1)

master.mainloop()