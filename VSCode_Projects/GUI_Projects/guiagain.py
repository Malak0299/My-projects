from tkinter import *
import customtkinter as c

c.set_appearance_mode("dark")
c.set_default_color_theme("dark-blue")

master = c.CTk()
master.title("Window")
master.geometry("500x500")

#PACK(i mid), GRID(venstre), PLACE
#label
label = c.CTkLabel(master, text = "Here I am")
label.grid(row = 0, column = 1, padx = 20, pady = 20)

def navn():
    label.configure(text = f'Hello {entry.get()}')
    entry.delete(0,END)
    entry.configure(state = "disabled")

def color_picker(choice):
    label.configure(text = choice, text_color = choice)

colors = ["Red", "Green", "Blue"]
combo = c.CTkComboBox(master, values = colors, command = color_picker)
combo.grid(row = 3, column = 0)

def ny():
    master.destroy

Button = c.CTkButton(master,
                     text = "Navn", 
                     command = navn,
                     height = 100,
                     width = 200,
                     font = ("Helvetica", 24),
                     text_color = "black",
                     fg_color = "blue", 
                     #background farve)
                     hover_color = "pink",
                     corner_radius = 20, 
                     #bg_color="white", #backgrundsfarve
                     border_width = 1,
                     border_color = "blue", 
                     #state = "disabled"
)
#button.pack(pady=80)
Button.grid(row = 1, column = 0)

entry = c.CTkEntry(master,
                   placeholder_text="Write your name")
entry.grid(row = 1, column = 1)


master.mainloop() #jeg skal altid stå til sidst