from tkinter import *

class LandingPanel:

    def __init__(self,root):
        self.root = root
    
    def genLanding(self):
        self.overallFrame = Frame(self.root,
                            width = 950,
                            height= 600)
        self.overallFrame.pack()