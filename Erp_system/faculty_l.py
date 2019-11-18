import tkinter 
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("F:/tArUN/programs/Python programs/erpsystem/Erp_system/Database/erp.db")
c = conn.cursor()

class Database:
    def __init__(self , master , *args , **kwargs):

        self.master= master
        # heading label
        self.heading = tkinter.Label(master, text="Faculty Information",  fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=300, y=0)
        
        #labels 
        self.search_l = tkinter.Label(master, text="Enter Faculty's Roll Number ", font=('arial 18 bold'))
        self.search_l.place(x=0, y=100)

        self.roll_l = tkinter.Label(master, text=" Roll Number", font=('arial 18 bold'))
        self.roll_l.place(x=0, y=200)

        self.name_l = tkinter.Label(master, text=" Name", font=('arial 18 bold'))
        self.name_l.place(x=0, y=300)

        self.sub_l = tkinter.Label(master, text=" Subject", font=('arial 18 bold'))
        self.sub_l.place(x=0, y=400)

        self.phone_l = tkinter.Label(master, text=" Phone", font=('arial 18 bold'))
        self.phone_l.place(x=0, y=500)

        #entries for labels
        self.search_e = tkinter.Entry(master, width=15, font=('arial 18 bold'))
        self.search_e.place(x=380 , y=100)

        self.roll_e = tkinter.Entry(master, width=30, font=('arial 18 bold'))
        self.roll_e.place(x=200 , y=200)

        self.name_e = tkinter.Entry(master, width=30, font=('arial 18 bold'))
        self.name_e.place(x=200 , y=300)

        self.sub_e = tkinter.Entry(master, width=30, font=('arial 18 bold'))
        self.sub_e.place(x=200 , y=400)

        self.phone_e = tkinter.Entry(master, width=30, font=('arial 18 bold'))
        self.phone_e.place(x=200 , y=500)

         #search db button
        self.btn_search = tkinter.Button(master, text="Search", width=20, height=2, bg='steelblue', command = self.search)
        self.btn_search.place(x=600, y=100)

    def search(self, *args, **kwargs):
        sql = "SELECT * FROM teacher WHERE id=?"
        result = c.execute(sql, (self.search_e.get(), ))
        for r in result:
            self.n1 = r[0] #roll
            self.n2 = r[1] #name
            self.n3 = r[2] #subject
            self.n4 = r[3] #phone
        conn.commit()

        # insert into the entries to update
        self.roll_e.config(state='normal')
        self.roll_e.delete(0, tkinter.END)
        self.roll_e.insert(0, str(self.n1))
        self.roll_e.config(state='readonly')

        self.name_e.config(state='normal')
        self.name_e.delete(0, tkinter.END)
        self.name_e.insert(0, str(self.n2))
        self.name_e.config(state='readonly')

        self.sub_e.config(state='normal')
        self.sub_e.delete(0, tkinter.END)
        self.sub_e.insert(0, str(self.n3))
        self.sub_e.config(state='readonly')

        self.phone_e.config(state='normal')
        self.phone_e.delete(0, tkinter.END)
        self.phone_e.insert(0, str(self.n4))
        self.phone_e.config(state='readonly')
  
# creating the object
root = tkinter.Tk()
b = Database(root)

root.geometry("1200x720+0+0")
root.title("Faculty Information")
root.mainloop()