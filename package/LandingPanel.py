from tkinter import *
from PIL import ImageTk, Image
import package.functions

class LandingPanel:

    def __init__(self,root):
        self.root = root
        self.img1 = ImageTk.PhotoImage(Image.open("img/mart1.jpg").resize((950,150)))
        self.img2 = ImageTk.PhotoImage(Image.open("img/mart2.jpg").resize((950,150)))
    
    def genLanding(self):
        self.overallFrame = Frame(self.root,
                            width = 950,
                            height= 600,
                            bg = 'BLUE')
        self.overallFrame.pack()

        mart1Img = Label(self.overallFrame,
                         image = self.img1,
                         borderwidth=0)
        mart1Img.image = self.img1
        mart1Img.grid(row=0,column=0,sticky='n')

        mart2Img = Label(self.overallFrame,
                         image = self.img2,
                         borderwidth=0)
        mart2Img.image = self.img2
        mart2Img.grid(row=3,column=0,sticky='s')

        body = Frame(self.overallFrame,
                     width = 950,
                     height= 300,
                     bg = "#565656")
        body.grid(row=1,column=0,sticky='n')

        companyLabel = Label(body, 
                            text = "AllMart\n I n c o r p o r a t e d",
                            font = ('Eras Bold ITC',60),
                            bg ='#565656',
                            fg = '#F2f7f9',
                            highlightthickness=2,
                            highlightbackground='#F2f7f9')
        companyLabel.place(relx =0.1,rely=0.1)

        temp = Button(body,
                      text = "NEXT",
                      command = lambda: [self.forgetLanding(),
                                         package.functions.showMain(self.root)])
        temp.place(relx=0.5,rely=0.8)



    def forgetLanding(self):
        self.overallFrame.destroy()