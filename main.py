
import weather

import tkinter as tk

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
    if loc.get() is "":
        tk.Label(root, text=('The temperature in %s is %sC' %
                             ('kathmandu', weather.currentTemp))).grid(row=5)
    else:
        tk.Label(root, text=('The temperature in %s is %sC' %
                             (loc.get(), weather.currentTemp))).grid(row=5)
    tk.Label(root, text=('It feels like %s C ' %
                         (weather.feelLike))).grid(row=6)


b1 = tk.Button(
    text="Submit", command=lambda: [weather.getWeatherUpdate(loc.get()), resultLabel()])
b1.grid(row=1, column=3)


# tk.Label(root, text=weather.feelNow).grid(row=6)


root.mainloop()


# function to get the weather of the required location
