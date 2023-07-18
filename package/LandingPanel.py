from tkinter import *
import package.functions

class LandingPanel:

    def __init__(self,root):
        self.root = root
    
    def genLanding(self):
        self.overallFrame = Frame(self.root,
                            width = 950,
                            height= 600,
                            bg = 'BLUE')
        self.overallFrame.pack()

    def forgetLanding(self):
        self.overallFrame.forget()