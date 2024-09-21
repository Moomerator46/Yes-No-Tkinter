import tkinter as th
from tkinter import ttk
from tkinter import messagebox
import random

choices = ['Yes', 'No']

window = tk.Tk()
window.title("Yes/No Randomizer")
window.geometry('400x300')

def choose():
  chosen = random.choice(choices)
  messagebox.showinfo("The choice was...", chosen+"!")

btn = ttk.Button(master=window, text="Get a Y/N answer", command=choose)
btn.pack()

window.mainloop()
