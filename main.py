
import weather
import io
import base64
import tkinter as tk
from tkinter import *
import urllib.request

from PIL import Image, ImageTk
root = tk.Tk()


# place a label on the root window
# Adjust size
root.title("Weather Check")
root.geometry("380x350")
tk.Label(root, text="API Key").grid(row=0)
tk.Label(root, text="Location").grid(row=1)

loc = tk.StringVar()
key = tk.StringVar()
API_Key = tk.Entry(root, textvariable=key).grid(row=0, column=1)
Location = tk.Entry(root, textvariable=loc).grid(row=1, column=1)

# All the labels for the weather


tk.Label(root, text=('/*----------------------------------------------------------------------*/')
         ).grid(row=3, columnspan=4, sticky='W')
Location = tk.Label(root, text=('Location :: ')).grid(
    row=4, column=0, sticky='W')
tk.Label(root, text=('Temperature :: ')).grid(row=5, column=0, sticky='W')
tk.Label(root, text=('Feels Like :: ')).grid(row=6, column=0, sticky='W')
tk.Label(root, text=('Wind :: ')).grid(row=7, column=0, sticky='W')
tk.Label(root, text=('Humidity :: ')).grid(row=8, column=0, sticky='W')
tk.Label(root, text=('Cloud :: ')).grid(row=9, column=0, sticky='W')

# The function to display the result


def resultLabel():

    if len(loc.get()) > 0:
        tk.Label(root, text=('')).grid(row=3, column=2, sticky='W')
        tk.Label(root, text=(loc.get())).grid(row=4, column=1, sticky='W')
    else:
        tk.Label(root, text=('kathmandu')).grid(row=4, column=1, sticky='W')

    tk.Label(root, text=(weather.currentTemp)).grid(
        row=5, column=1, sticky='W')
    tk.Label(root, text=(weather.feelLike)).grid(row=6, column=1, sticky='W')
    tk.Label(root, text=(weather.wind)).grid(row=7, column=1, sticky='W')
    tk.Label(root, text=(weather.humidity)).grid(row=8, column=1, sticky='W')
    tk.Label(root, text=(weather.cloud)).grid(row=9, column=1, sticky='W')

    weatherurl = 'https:' + weather.icon
    urllib.request.urlretrieve(
        weatherurl,
        "weather.png")

    image = Image.open("weather.png")
    imgWidth = 100
    imgHeight = (imgWidth/image.width) * float(image.height)

    resizeImage = image.resize((int(imgWidth), int(imgHeight)))
    photo = ImageTk.PhotoImage(resizeImage)

    labelP = Label(image=photo, bg="#C2C2C2")
    labelP.image = photo  # keep a reference!

    labelP.grid(row=10, column=1)


b1 = tk.Button(
    text="Submit", command=lambda: [weather.getWeatherUpdate(loc.get(), key.get()), resultLabel()])
b1.grid(row=1, column=3)


root.mainloop()
