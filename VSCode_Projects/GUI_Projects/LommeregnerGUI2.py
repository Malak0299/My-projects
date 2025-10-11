from tkinter import *
import customtkinter as c

c.set_appearance_mode("dark")
window = c.CTk()
window.geometry("560x200")
window.title("Lommeregner")

udtryk = ""

def tryk(key):
    global udtryk
    udtryk = udtryk + str(key)
    label.configure(text = str(udtryk))

def clear():
    global udtryk
    udtryk = ""
    label.configure(text = str(udtryk))

def ligmed():
    global udtryk
    try:
        result = str(eval(udtryk))
        label.configure(text = result)
        udtryk = ""
    except:
        label.configure(text = "ERROR")
        udtryk = ""



label = c.CTkLabel(window, text_color = "orange", text = "", font = ("", 29))
label.grid(row = 0, column = 0, columnspan = 4)

knapce = c.CTkButton(window, text = 'CE', fg_color = 'blue', hover_color = 'grey',command = clear)
knapce.grid(row = 1, column = 0)
knap1 = c.CTkButton(window, text = '1', fg_color = 'blue', hover_color = 'grey', command = lambda: tryk(1))
knap1.grid(row = 2, column = 0)
knap2 = c.CTkButton(window, text = '2', fg_color = 'blue', hover_color = 'grey', command = lambda: tryk(2))
knap2.grid(row = 2, column = 1)
knap3 = c.CTkButton(window, text = '3', fg_color = 'blue', hover_color = 'grey', command = lambda: tryk(3))
knap3.grid(row = 2, column = 2)
knapd = c.CTkButton(window, text = '/', fg_color = 'red', hover_color = 'grey', command = lambda: tryk("/"))
knapd.grid(row = 2, column = 3)
knap4 = c.CTkButton(window, text = '4', fg_color = 'blue', hover_color = 'grey', command = lambda: tryk(4))
knap4.grid(row = 3, column = 0)
knap5 = c.CTkButton(window, text = '5', fg_color = 'blue', hover_color = 'grey', command = lambda: tryk(5))
knap5.grid(row = 3, column = 1)
knap6 = c.CTkButton(window, text = '6', fg_color = 'blue', hover_color = 'grey', command = lambda: tryk(6))
knap6.grid(row = 3, column = 2)
knapg = c.CTkButton(window, text = '*', fg_color = 'red', hover_color = 'grey', command = lambda: tryk("*"))
knapg.grid(row = 3, column = 3)
knap7 = c.CTkButton(window, text = '7', fg_color = 'blue', hover_color = 'grey', command = lambda: tryk(7))
knap7.grid(row = 4, column = 0)
knap8 = c.CTkButton(window, text = '8', fg_color = 'blue', hover_color = 'grey', command = lambda: tryk(8))
knap8.grid(row = 4, column = 1)
knap9 = c.CTkButton(window, text = '9', fg_color = 'blue', hover_color = 'grey', command = lambda: tryk(9))
knap9.grid(row = 4, column = 2)
knapm = c.CTkButton(window, text = '-', fg_color = 'red', hover_color = 'grey', command = lambda: tryk("-"))
knapm.grid(row = 4, column = 3)
knapp = c.CTkButton(window, text = '.', fg_color = 'red', hover_color = 'grey', command = lambda: tryk("."))
knapp.grid(row = 5, column = 0)
knap0 = c.CTkButton(window, text = '0', fg_color = 'blue', hover_color = 'grey', command = lambda: tryk(0))
knap0.grid(row = 5, column = 1)
knapl = c.CTkButton(window, text = '=', fg_color = 'red', hover_color = 'grey',command = ligmed)
knapl.grid(row = 5, column = 2)
knappl = c.CTkButton(window, text = '+', fg_color = 'red', hover_color = 'grey', command = lambda: tryk("+"))
knappl.grid(row = 5, column = 3)
knapfa = c.CTkButton(window, text = '!', fg_color = 'blue', hover_color = 'grey', command = lambda: tryk("!"))
knapfa.grid(row = 3, column = 4)
knapnn = c.CTkButton(window, text = '00', fg_color = 'blue', hover_color = 'grey', command = lambda: tryk(10))
knapnn.grid(row = 4, column = 4)
knappc = c.CTkButton(window, text = '%', fg_color = 'blue', hover_color = 'grey', command = lambda: tryk("%"))
knappc.grid(row = 5, column = 4)

#OPGAVE KNAPPER
knapro = c.CTkButton(window, text = '√', fg_color = 'blue', hover_color = 'grey', command = lambda: tryk(","))
knapro.grid(row = 2, column = 4)



window.mainloop()