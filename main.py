from tkinter import *
from tkinter import ttk
import customtkinter
from package.functions import *

root = customtkinter.CTk()
root.title('ALLMART INC. INVENTORY SYSTEM')
root.geometry("950x600")
style = ttk.Style(root)
style.theme_use("clam")

showLanding(root)

root.resizable(False,False)
root.eval('tk::PlaceWindow . center')
root.mainloop()

