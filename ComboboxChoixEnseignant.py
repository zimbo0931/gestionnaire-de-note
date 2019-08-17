
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.minsize(600, 400)
window.title("choix prof principal")



def choixEnseignant():
    label.configure(text="Choisissez" + mynumber.get())


label = ttk.Label(window, text = "Choix de l'enseignant")
label.grid(column=0, row=0)

mynumber = tk.StringVar()
combobox = ttk.Combobox(window, width=15, textvariable=mynumber)
combobox['values'] = ('Aristouin Philippe', 'Baudin Jean-Marc', 'Calvieres Thérèse', 'Durand Marc', 'Elliot James', 'Francesco Sylvie', 'Guerin Serge')


combobox.grid(column=1, row=0)

button = ttk.Button(window, text="Valider", command=choixEnseignant())
button.grid(column=1, row=1)

window.mainloop()