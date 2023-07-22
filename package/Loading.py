from tkinter import *
import time
import package.functions

class Loading:

    def __init__(self,root):
        self.root = root
    
    def genLoading(self):
        self.overallFrame = Frame(self.root,
                            width = 950,
                            height= 600,
                            bg = "#565656")
        self.overallFrame.pack()

        loadingLbl = Label(self.overallFrame,
                           text = "P L E A S E  W A I T . . . .",
                           font = ('Arial',30),
                           bg ='#565656',
                           fg = '#F2f7f9')
        loadingLbl.place(relx=0.3,rely=0.5)


    def forgetLoading(self):
        self.overallFrame.destroy()
        package.functions.showMain(self.root)
        