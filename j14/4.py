# import tkinter as tk
from tkinter import *


bg_color = "#239943"

window = Tk()

window.geometry("400x450")
window.title("first application")

window.config(background=bg_color)

window.resizable(True, False)

window.mainloop()