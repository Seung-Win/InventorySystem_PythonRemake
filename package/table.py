from tkinter import *
from tkinter import ttk

class Table:
    def __init__(self,overall):
        self.overall = overall

    def genTable(self):
        tableFrame = Frame(self.overall,
                        width = 550,
                        height= 550,
                        bg = "#565656",
                        highlightbackground="black",
                        highlightthickness=2)
        tableFrame.grid(row=1,rowspan=2,columnspan=1,sticky='E')
        tree = ttk.Treeview(tableFrame,
                            height=23)
        tree['show']='headings'
        tree["columns"] = ("product_ID","product_Name","product_Desc","product_Price","product_Avail","product_Stock","product_Date")

        tree.column("product_ID",width=50, minwidth=50)
        tree.column("product_Name",width=75, minwidth=70)
        tree.column("product_Desc",width=97, minwidth=97)
        tree.column("product_Price",width=70, minwidth=70)
        tree.column("product_Avail",width=100, minwidth=100)
        tree.column("product_Stock",width=50, minwidth=50)
        tree.column("product_Date",width=100, minwidth=100)

        tree.heading("product_ID", text="ID")
        tree.heading("product_Name", text="Name")
        tree.heading("product_Desc", text="Description")
        tree.heading("product_Price", text="Price")
        tree.heading("product_Avail", text="Availability")
        tree.heading("product_Stock", text="Stock")
        tree.heading("product_Date", text="Delivery Date")
        tree.place(x=0,y=0)

        searchArea = Entry(tableFrame,
                        width = 25)
        searchArea.focus()
        searchArea.bind("<Return>")
        searchArea.place(x=130,y=505)

        searchButton = Button(tableFrame,
                      text = "SEARCH",
                      height = 1,
                      width = 15)
        searchButton.place(x=10,y=503)

        refreshButton = Button(tableFrame,
                            text = "REFRESH",
                            height = 1,
                            width = 15)
        refreshButton.place(x=400,y=503)