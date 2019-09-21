import tkinter 
import sqlite3

conn = sqlite3.connect("F:/tArUN/programs/Python programs/erpsystem/Erp_system/Database/erp.db")
c = conn.cursor

class Database:
    def __init__(self , master , *args , **kwargs):

        self.master= master
        # heading label
        self.heading = tkinter.Label(master, text="Add to Database",  fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)
     

# creating the object
root = tkinter.Tk()
b = Database(root)

root.geometry("1200x720+0+0")
root.title("Add to Database")
root.mainloop()