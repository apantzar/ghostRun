#!/usr/bin/env python
import random
import subprocess

print("Installing packages for you...")
print()
subprocess.call("sudo apt-get install python3-tk", shell=True)

import tkinter as tk
from tkinter import *

from tkinter.constants import BOTTOM

changeStat = ""


def cover():
    global changeStat
    changeStat = "ghostRun"
    label.config(text=changeStat)

    list = ['FR', 'GR', 'US', 'AD', 'AE', 'HK', 'DE', 'CY', 'IL', 'ID', 'BS', 'KE', 'JP', 'GL', 'ES', 'CH', 'AT', 'AM']
    country = random.choice(list)
    print(country)
    subprocess.call("sudo cyberghostvpn --stop", shell=True)

    subprocess.call("cyberghostvpn --country-code " + country + " --connect", shell=True)


top = tk.Tk()
top.geometry('400x300')
destroy = tk.Button(text="Connect VPN", fg='blue', width=400, command=cover)
destroy.grid(row=0, column=3, padx=100)
destroy.pack(side=BOTTOM)

label = tk.Label(text="ghostRun", name="label-status")
label.pack()

top.mainloop()
