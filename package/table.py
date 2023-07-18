from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import package.MainPanel

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
        self.tree = ttk.Treeview(tableFrame,
                            height=23)
        self.tree['show']='headings'
        self.tree["columns"] = ("product_ID","product_Name","product_Desc","product_Price","product_Avail","product_Stock","product_Date")

        self.tree.column("product_ID",width=50, minwidth=50)
        self.tree.column("product_Name",width=75, minwidth=70)
        self.tree.column("product_Desc",width=97, minwidth=97)
        self.tree.column("product_Price",width=70, minwidth=70)
        self.tree.column("product_Avail",width=100, minwidth=100)
        self.tree.column("product_Stock",width=50, minwidth=50)
        self.tree.column("product_Date",width=100, minwidth=100)

        self.tree.heading("product_ID", text="ID")
        self.tree.heading("product_Name", text="Name")
        self.tree.heading("product_Desc", text="Description")
        self.tree.heading("product_Price", text="Price")
        self.tree.heading("product_Avail", text="Availability")
        self.tree.heading("product_Stock", text="Stock")
        self.tree.heading("product_Date", text="Delivery Date")
        self.tree.place(x=0,y=0)

        self.searchArea = Entry(tableFrame,
                        width = 25)
        self.searchArea.focus()
        self.searchArea.bind("<Return>")
        self.searchArea.place(x=130,y=505)

        searchButton = Button(tableFrame,
                      text = "SEARCH",
                      height = 1,
                      width = 15,
                      command = self.search)
        searchButton.place(x=10,y=503)

        refreshButton = Button(tableFrame,
                            text = "REFRESH",
                            height = 1,
                            width = 15,
                            command = self.refresh)
        refreshButton.place(x=400,y=503)
        

    def refresh(self):
        try:
            self.mydb = mysql.connector.connect(
                    host="sql6.freesqldatabase.com",
                    user="sql6631133",
                    password = "jVZZYlldxc",
                    database="sql6631133"
                    )
            self.tree.delete(*self.tree.get_children())
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute("SELECT * FROM product")
            for r in self.mycursor:
                self.tree.insert('','end',text="",values=(r[0],r[1],r[2],r[3],r[4],r[5],r[6]))
        except:
            messagebox.showinfo("Message","Error Refreshing Database!")

    def onClick(self,event):
        for parent in self.tree.selection():
            selected = self.tree.item(parent,"values")[0]
        self.mycursor.execute("SELECT * FROM product WHERE product_ID = %s",(selected,))
        record  = self.mycursor.fetchall()
        for r in record:
            id_value = r[0]
            name_value=r[1]
            desc_value = r[2]
            price_value =r[3]
            avail_value =r[4]
            stock_value =r[5]
            delivery_value =r[6]
        #Create Instance of Main Panel
        root = self.overall.winfo_toplevel()

        # Check if the root window has an instance of MainPanel
        if hasattr(root, "main_panel"):
            main_panel = root.main_panel
            main_panel.informationFrame(id_value, name_value, desc_value, price_value, avail_value, stock_value, delivery_value)
        
    def bind(self):
        self.tree.bind("<<TreeviewSelect>>", self.onClick)
    
    def search(self):
        try:
            mydb = mysql.connector.connect(
                host="sql6.freesqldatabase.com",
                user="sql6631133",
                password = "jVZZYlldxc",
                database="sql6631133"
                )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM product WHERE product_id = %s",(self.searchArea.get(),))
            myresult = mycursor.fetchall()
            self.tree.delete(*self.tree.get_children())
            for r in myresult:
                self.tree.insert('','end',text="",values=(r[0],r[1],r[2],r[3],r[4],r[5],r[6]))
        except:
            messagebox.showinfo("Message","ID Not Found!")


