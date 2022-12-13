
import weather

import tkinter as tk
from tkinter import *
root = tk.Tk()


# place a label on the root window
# Adjust size
root.geometry("500x500")
tk.Label(root, text="API Key").grid(row=0)
tk.Label(root, text="Location").grid(row=1)

loc = tk.StringVar()
API_Key = tk.Entry(root).grid(row=0, column=1)
Location = tk.Entry(root, textvariable=loc).grid(row=1, column=1)


def resultLabel():
    tk.Label(root, text=('Location :: ')).grid(row=3, column=1, sticky='W')
    kath = tk.Label(root, text=('kathmandu')).grid(row=3, column=2, sticky='W')
    if len(loc.get()) > 0:
        kath = tk.Label(root, text=('')).grid(row=3, column=2, sticky='W')
        kath = tk.Label(root, text=(loc.get())).grid(row=3, column=2, sticky='W')
        # tk.Label(root, text=('kathmandu')).grid(row=3, column=2, sticky='W')

    tk.Label(root, text=('Temperature :: ')).grid(row=4, column=1, sticky='W')
    tk.Label(root, text=(weather.feelLike)).grid(row=4, column=2, sticky='W')


b1 = tk.Button(
    text="Submit", command=lambda: [weather.getWeatherUpdate(loc.get()), resultLabel()])
b1.grid(row=1, column=3)


# tk.Label(root, text=weather.feelNow).grid(row=6)


root.mainloop()


# function to get the weather of the required location
