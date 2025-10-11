from tkinter import *
import customtkinter as c

c.set_appearance_mode("dark")
c.set_default_color_theme("dark-blue")

master = c.CTk()
master.title("Window")
master.geometry("500x500")

#PACK(i mid), GRID(venstre), PLACE
#PACK
label = c.CTkLabel(master, text = "Here I am")
label.pack(pady = 10)

#GRID
label = c.CTkLabel(master, text = "Here I am")
label.grid(row = 0, column = 1, padx = 20, pady = 20)

#PRØV AT INDSÆTTE ANDRE TING
Button = c.CTkButton(master,
                     text = "Navn", 
                     #Command = navn
                     height = 100,
                     width = 200,
                     font = ("Helvetica", 24),
                     text_color = "black",
                     fg_color = "blue", 
                     #background farve)
                     hover_color = "yellow",
                     corner_radius = 20, 
                     #bg_color="white", #backgrundsfarve
                     border_width = 1,
                     border_color = "blue", 
                     #state = "disabled"
)
#button.pack(pady=80)
Button.grid(row = 1, column = 0)

master.mainloop() #jeg skal altid stå til sidst