from tkinter import *
from tkinter import ttk
from package.MainPanel import *

root = Tk()
root.title('ALLMART INC. INVENTORY SYSTEM')
root.geometry("950x600")
style = ttk.Style(root)
style.theme_use("clam")

mainPanel = MainPanel(root)
mainPanel.genMainPanel()


