
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.minsize(600, 400)
window.title("choix prof principal")



def chosingNumbers():
    label.configure(text="Vous avez choisit" + mynumber.get())


label = ttk.Label(window, text = "Choix de l'année")
label.grid(column=0, row=0)

mynumber = tk.StringVar()
combobox = ttk.Combobox(window, width=15, textvariable=mynumber)
combobox['values'] = ('2014-2015', '2015-2016', '2016-2017', '2017-2018', '2018-2019', '2019-2020')
combobox.grid(column=1, row=0)

button = ttk.Button(window, text="Valider", command=chosingNumbers)
button.grid(column=1, row=1)

window.mainloop()