import package.LandingPanel 
import package.MainPanel
import package.table
import package.Loading
from tkinter import messagebox
import mysql.connector


def showLanding(root):
    landing = package.LandingPanel.LandingPanel(root)
    landing.genLanding()

def showMain(root):
    main = package.MainPanel.MainPanel(root)
    main.genMainPanel()

def showLoading(root):
    loading = package.Loading.Loading(root)
    loading.genLoading()
    root.after(1000,loading.forgetLoading)
    

def insertMsg(idVal,nameVal,descVal,priceVal,availVal,stockVal,dateVal):
    if (idVal=="" or nameVal=="" or descVal=="" or priceVal=="" or availVal=="" or stockVal=="" or dateVal==""):
        messagebox.showinfo("Message","Please Input All Fields!")
    else:
        try:
            mydb = mysql.connector.connect(
                host="sql6.freesqldatabase.com",
                user="sql6631133",
                password = "jVZZYlldxc",
                database="sql6631133"
                )
            mycursor = mydb.cursor()

            sql = "INSERT INTO product (product_ID,product_Name,product_Desc,product_Price,product_Avail,product_Stock,product_Date) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            val  = (idVal,nameVal,descVal,priceVal,availVal,stockVal,dateVal)
            mycursor.execute(sql,val)
            mydb.commit()
        except:
            messagebox.showinfo("Message","Insertion Failed!")
        else:
            messagebox.showinfo("Message","Insertion Success!")
    
def deleteMsg(idVal):
    if (idVal==""):
        messagebox.showinfo("Message","Please Input Product ID!")
    else:
        try:
            mydb = mysql.connector.connect(
                host="sql6.freesqldatabase.com",
                user="sql6631133",
                password = "jVZZYlldxc",
                database="sql6631133"
                )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT product_id FROM product WHERE product_ID = %s",(idVal,))
            mycursor.fetchall()
            if (mycursor.rowcount == 0):
                messagebox.showinfo("Message","ID Not Found!")
            else:
                try:
                    sql = "DELETE FROM product WHERE product_ID = %s"
                    val = (idVal,)
                    mycursor.execute(sql,val)
                    mydb.commit()
                except:
                    messagebox.showinfo("Message","Deletion Failed!")
                else:
                    messagebox.showinfo("Message","Deletion Success!")
        except:
            messagebox.showinfo("Message","Query Failed!")

            

def updateMsg(idVal,nameVal,descVal,priceVal,availVal,stockVal,dateVal):
    if (idVal=="" or nameVal=="" or descVal=="" or priceVal=="" or availVal=="" or stockVal=="" or dateVal==""):
        messagebox.showinfo("Message","Please Input All Fields!")
    else:
        try:
            mydb = mysql.connector.connect(
                host="sql6.freesqldatabase.com",
                user="sql6631133",
                password = "jVZZYlldxc",
                database="sql6631133"
                )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM product WHERE product_ID = %s",(idVal,))
            mycursor.fetchall()
            if (mycursor.rowcount == 0):
                messagebox.showinfo("Message","ID Not Found!")
            else:
                try:
                    sql = "UPDATE product SET product_Name = %s,product_Desc = %s,product_Price = %s,product_Avail = %s,product_Stock = %s,product_Date = %s WHERE product_ID = %s"
                    val = (nameVal,descVal,priceVal,availVal,stockVal,dateVal,idVal,)
                    mycursor.execute(sql,val)
                    mydb.commit()
                except:
                    messagebox.showinfo("Message","Update Failed!")
                else:
                    messagebox.showinfo("Message","Update Success!")
        except:
            messagebox.showinfo("Message","Query Failed!")
