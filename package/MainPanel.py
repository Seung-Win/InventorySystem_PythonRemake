from tkinter import *
from tkcalendar import DateEntry
import customtkinter
from package.table import *
import package.functions
from PIL import Image

class MainPanel:
    def __init__(self,root):
        self.root = root
        self.sel = StringVar()
        self.addIcon = customtkinter.CTkImage(Image.open("img/add.png").resize((20,20),Image.LANCZOS))
        self.delIcon = customtkinter.CTkImage(Image.open("img/delete.png").resize((20,20),Image.LANCZOS))
        self.updateIcon = customtkinter.CTkImage(Image.open("img/update.png").resize((20,20),Image.LANCZOS))
        self.logoutIcon = customtkinter.CTkImage(Image.open("img/logout.png").resize((20,20),Image.LANCZOS))
        self.idValue = None
        self.nameValue = None
        self.descValue = None
        self.priceValue = None
        self.availValue = None
        self.stockValue = None
        self.deliveryValue = None

    def genMainPanel(self):
        #Create the UI
        self.overallFrame = Frame(self.root,
                            width = 950,
                            height= 600)
        self.overallFrame.pack()
        headerFrame = Frame(self.overallFrame,
                        width = 950,
                        height= 50,
                        bg = "#565656",
                        highlightbackground="#565656",
                        highlightthickness=2)
        headerFrame.grid(column=0, row=0, sticky='n')

        companyLabel = Label(headerFrame, 
                            text = "A l l M a r t   I n c .",
                            font = ('Eras Bold ITC',25),
                            bg ='#565656',
                            fg = '#F2f7f9')
        companyLabel.place(x =20,y=2)

        backButton = customtkinter.CTkButton(master=headerFrame,
                                             image = self.logoutIcon,
                                             text = "Log Out",
                                             fg_color = "#ebebeb",
                                             text_color = "#0f0f0f",
                                             width = 50,
                                             height = 20,
                                             command = lambda: [self.forgetMainPanel(),
                                                                package.functions.showLanding(self.root)])
        backButton.place(relx=0.9,rely=0.3)

        #Form
        form1Frame = Frame(self.overallFrame,
                    width = 400,
                    height= 320,
                    bg = "#A0A1A4",
                    highlightbackground="#A0A1A4",
                    highlightthickness=2)
        form1Frame.grid(column=0,row=1,sticky='w')

        form2Frame = Frame(self.overallFrame,
                    width = 400,
                    height= 230,
                    bg = "#A0A1A4",
                    highlightbackground="#A0A1A4",
                    highlightthickness=2)
        form2Frame.grid(column=0,row=2,sticky='w')

        #Form1Labels
        infoLabel = Label(form1Frame,
                        text = "Enter Product Information",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        infoLabel.place(x=115,y=5)

        idLabel = Label(form1Frame,
                        text = "Product ID: ",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        idLabel.place(x=5,y=30)

        nameLabel = Label(form1Frame,
                        text = "Product Name: ",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        nameLabel.place(x=5,y=60)

        descLabel = Label(form1Frame,
                        text = "Product Description: ",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        descLabel.place(x=5,y=90)

        priceLabel = Label(form1Frame,
                        text = "Product Price: ",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        priceLabel.place(x=5,y=120)

        availLabel = Label(form1Frame,
                        text = "Product Availabilty: ",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        availLabel.place(x=5,y=150)

        stockLabel = Label(form1Frame,
                        text = "Stock Left: ",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        stockLabel.place(x=5,y=180)

        deliveryLabel = Label(form1Frame,
                        text = "Delivery Date: ",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        deliveryLabel.place(x=5,y=210)

        noteLabel = Label(form1Frame,
                        text = "Deletion Requires ID Only",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4",
                        fg = "RED")
        noteLabel.place(x=105,y=290)

        #Form1 Text Fields 
        idTxtField = Entry(form1Frame,
                        width = 25)
        idTxtField.focus()
        idTxtField.bind("<Return>",lambda e:nameTxtField.focus())
        idTxtField.place(x=150,y=30)

        nameTxtField = Entry(form1Frame,
                        width = 25)
        nameTxtField.focus()
        nameTxtField.bind("<Return>",lambda e:descTxtField.focus())
        nameTxtField.place(x=150,y=60)

        descTxtField = Entry(form1Frame,
                        width = 25)
        descTxtField.focus()
        descTxtField.bind("<Return>",lambda e:priceTxtField.focus())
        descTxtField.place(x=150,y=90)

        priceTxtField = Entry(form1Frame,
                        width = 25)
        priceTxtField.focus()
        priceTxtField.bind("<Return>",lambda e:stockTxtField.focus())
        priceTxtField.place(x=150,y=120)
        
        availRadButtonY = Radiobutton(form1Frame,
                                    text="Yes",
                                    bg = "#A0A1A4",
                                    value = "Yes",
                                    variable = self.sel)
        availRadButtonY.place(x=150,y=150)

        availRadButtonN = Radiobutton(form1Frame,
                                    text="No",
                                    bg = "#A0A1A4",
                                    value = "No",
                                    variable = self.sel)
        availRadButtonN.place(x=210,y=150)

        stockTxtField = Entry(form1Frame,
                        width = 25)
        stockTxtField.focus()
        stockTxtField.bind("<Return>",lambda e:idTxtField.focus())
        stockTxtField.place(x=150,y=180)

        availDateEntry = DateEntry(form1Frame,
                                selectmode = 'day')
        availDateEntry.place(x=150,y=210)
        dt = availDateEntry.get_date()
        str_dt = dt.strftime("%Y-%m-%d")

        #Form2 Labels
        infoLabel2 = Label(form2Frame,
                        text = "Product Information",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        infoLabel2.place(x=130,y=5)

        idLabel2 = Label(form2Frame,
                        text = "Product ID: ",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        idLabel2.place(x=5,y=30)

        nameLabel2 = Label(form2Frame,
                        text = "Product Name: ",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        nameLabel2.place(x=5,y=55)

        descLabel2 = Label(form2Frame,
                        text = "Product Description: ",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        descLabel2.place(x=5,y=80)

        priceLabel2 = Label(form2Frame,
                        text = "Product Price: ",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        priceLabel2.place(x=5,y=105)

        availLabel2 = Label(form2Frame,
                        text = "Product Availabilty: ",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        availLabel2.place(x=5,y=130)

        stockLabel2 = Label(form2Frame,
                        text = "Stock Left: ",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        stockLabel2.place(x=5,y=155)

        deliveryLabel2 = Label(form2Frame,
                        text = "Delivery Date: ",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        deliveryLabel2.place(x=5,y=180)

        #Form2 Values
        self.idValue = Label(form2Frame,
                        text = "",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        self.idValue.place(x=150,y=30)

        self.nameValue = Label(form2Frame,
                        text = "",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        self.nameValue.place(x=150,y=55)

        self.descValue = Label(form2Frame,
                        text = "",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        self.descValue.place(x=150,y=80)

        self.priceValue = Label(form2Frame,
                        text = "",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        self.priceValue.place(x=150,y=105)

        self.availValue = Label(form2Frame,
                        text = "",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        self.availValue.place(x=150,y=130)

        self.stockValue = Label(form2Frame,
                        text = "",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        self.stockValue.place(x=150,y=155)

        self.deliveryValue = Label(form2Frame,
                        text = "",
                        font = ('ARIAL',10,'bold'),
                        bg = "#A0A1A4")
        self.deliveryValue.place(x=150,y=180)

        #Create Table Instance
        table = Table(self.overallFrame)
        table.genTable()
        table.refresh()
        table.bind()
        self.root.main_panel = self

        #Buttons
        insertButton = customtkinter.CTkButton(form1Frame,
                                               image = self.addIcon,
                                               text = "INSERT",
                                               height = 20,
                                               width = 50,
                                               fg_color = "#ebebeb",
                                               text_color = "#0f0f0f",
                                               command = lambda:[package.functions.insertMsg(idTxtField.get(),
                                                                            nameTxtField.get(),
                                                                            descTxtField.get(),
                                                                            priceTxtField.get(),
                                                                            self.sel.get(),
                                                                            stockTxtField.get(),
                                                                            str_dt),
                                                                    table.refresh()])
        insertButton.place(x=15,y=250)

        updateButton = customtkinter.CTkButton(form1Frame,
                                               image = self.updateIcon,
                                               text = "UPDATE",
                                               height = 20,
                                               width = 50,
                                               fg_color = "#ebebeb",
                                               text_color = "#0f0f0f",
                                               command = lambda: [package.functions.updateMsg(idTxtField.get(),
                                                                    nameTxtField.get(),
                                                                    descTxtField.get(),
                                                                    priceTxtField.get(),
                                                                    self.sel.get(),
                                                                    stockTxtField.get(),
                                                                    str_dt),
                                                            table.refresh()])
        updateButton.place(x=140,y=250)

        deleteButton = customtkinter.CTkButton(form1Frame,
                                               image = self.delIcon,
                                               text = "DELETE",
                                               height = 20,
                                               width = 50,
                                               fg_color = "#ebebeb",
                                               text_color = "#0f0f0f",
                                               command = lambda: [package.functions.deleteMsg(idTxtField.get()),
                                                        table.refresh()])
        deleteButton.place(x=265,y=250)

    def informationFrame(self, id_value, name_value, desc_value, price_value, avail_value, stock_value, delivery_value):
        self.idValue.config(text=id_value)
        self.nameValue.config(text=name_value)
        self.descValue.config(text=desc_value)
        self.priceValue.config(text=price_value)
        self.availValue.config(text=avail_value)
        self.stockValue.config(text=stock_value)
        self.deliveryValue.config(text=delivery_value)

    def forgetMainPanel(self):
        self.overallFrame.destroy()