from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import package.functions

class LandingPanel:

    def __init__(self,root):
        self.root = root
        self.img1 = ImageTk.PhotoImage(Image.open("img/mart1.jpg").resize((950,150)))
        self.img2 = ImageTk.PhotoImage(Image.open("img/mart2.jpg").resize((950,150)))
        self.nextIcon = customtkinter.CTkImage(Image.open("img/next.png").resize((20,20),Image.LANCZOS))
        self.backIcon = customtkinter.CTkImage(Image.open("img/back.png").resize((30,30),Image.LANCZOS))
    
    def genLanding(self):
        self.overallFrame = Frame(self.root,
                            width = 950,
                            height= 600)
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

        self.genInit()

    
    def genInit(self):
        self.body = Frame(self.overallFrame,
                     width = 950,
                     height= 300,
                     bg = "#565656")
        self.body.grid(row=1,column=0,sticky='n')

        companyLabel = Label(self.body, 
                            text = "AllMart\n I n c o r p o r a t e d ",
                            font = ('Eras Bold ITC',60),
                            bg ='#565656',
                            fg = '#F2f7f9',
                            highlightthickness=2,
                            highlightbackground='#F2f7f9')
        companyLabel.place(relx =0.08,rely=0.1)

        nextButton = customtkinter.CTkButton(self.body,
                                       text = "NEXT",
                                       image = self.nextIcon,
                                       height = 30,
                                       width = 60,
                                       fg_color = "#ebebeb",
                                       text_color = "#0f0f0f",
                                       command = lambda: [self.body.destroy(),
                                                self.genLogin()])
        nextButton.place(relx=0.46,rely=0.8)

    def genLogin(self):
        self.body = Frame(self.overallFrame,
                     width = 950,
                     height= 300,
                     bg = "#565656")
        self.body.grid(row=1,column=0,sticky='n')

        greetLbl = Label(self.body, 
                            text = " Greetings Admin! ",
                            font = ('Eras Bold ITC',50),
                            bg ='#565656',
                            fg = '#F2f7f9',
                            highlightthickness=2,
                            highlightbackground='#F2f7f9')
        greetLbl.place(relx =0.16,rely=0.1)

        userLbl = Label(self.body,
                        text = "Username:",
                        font = ('Arial', 20),
                        bg = '#565656',
                        fg = '#F2f7f9')
        userLbl.place(relx=0.2, rely=0.5)

        passbl = Label(self.body,
                        text = "Password:",
                        font = ('Arial', 20),
                        bg = '#565656',
                        fg = '#F2f7f9')
        passbl.place(relx=0.2, rely=0.7)

        backButton = customtkinter.CTkButton(self.body,
                                       image = self.backIcon,
                                       text = "",
                                       height = 30,
                                       width = 30,
                                       fg_color = "#ebebeb",
                                       command = lambda: [self.body.destroy(),
                                                self.genInit()])
        backButton.place(relx=0.05,rely=0.05)

    def forgetLanding(self):
        self.overallFrame.destroy()