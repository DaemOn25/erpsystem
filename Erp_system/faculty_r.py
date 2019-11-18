import tkinter 
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("F:/tArUN/programs/Python programs/erpsystem/Erp_system/Database/erp.db")
c = conn.cursor()

class Database:
    def __init__(self , master , *args , **kwargs):

        self.master= master
        # heading label
        self.heading = tkinter.Label(master, text="Faculty Registration",  fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=450, y=0)
        
        #labels 
        self.roll_l = tkinter.Label(master, text="Enter Faculty's Roll Number", font=('arial 18 bold'))
        self.roll_l.place(x=0, y=100)

        self.name_l = tkinter.Label(master, text="Enter Faculty's Name", font=('arial 18 bold'))
        self.name_l.place(x=0, y=200)

        self.sub_l = tkinter.Label(master, text="Enter Faculty's Subject", font=('arial 18 bold'))
        self.sub_l.place(x=0, y=300)

        self.phone_l = tkinter.Label(master, text="Enter Faculty's Phone", font=('arial 18 bold'))
        self.phone_l.place(x=0, y=400)

        #entries for labels
        self.roll_e = tkinter.Entry(master, width=30, font=('arial 18 bold'))
        self.roll_e.place(x=380 , y=100)

        self.name_e = tkinter.Entry(master, width=30, font=('arial 18 bold'))
        self.name_e.place(x=380 , y=200)

        self.sub_e = tkinter.Entry(master, width=30, font=('arial 18 bold'))
        self.sub_e.place(x=380 , y=300)

        self.phone_e = tkinter.Entry(master, width=30, font=('arial 18 bold'))
        self.phone_e.place(x=380 , y=400)

         # add to db button
        self.btn_add = tkinter.Button(master, text="ADD", width=20, height=2, bg='steelblue', command = self.write_fac)
        self.btn_add.place(x=585, y=550)

         # clear field button
        self.btn_clr = tkinter.Button(master, text="CLEAR", width=20, height=2, bg='steelblue', command = self.clear_all)
        self.btn_clr.place(x=400, y=550)

        # text box for logs
        self.tBox = tkinter.Text(master , width = 60, height = 27)
        self.tBox.place(x=850 ,  y= 100)
    
    def write_fac(self , *args , **kwargs):
        #get from entries
        self.roll = self.roll_e.get()
        self.name = self.name_e.get()      
        self.sub = self.sub_e.get()
        self.phone = self.phone_e.get()

        if self.name == '' or  self.roll == '' or self.sub == '' or self.phone == '' :
            tkinter.messagebox.showwarning("Warning" , "PLEASE FILL ALL THE ENTRIES")
        else:
            
            sql = "INSERT INTO teacher ( id , name , subject , phone) VALUES(?,?,?,?)"
            c.execute(sql , (self.roll , self.name , self.sub , self.phone))
            conn.commit()
            #text box msg
            self.tBox.insert(tkinter.END, "\n\n Inserted " + str(self.name) + " into the database\n with roll id = " + str(self.roll_e.get()))

            tkinter.messagebox.showinfo("Success" , "Successfully added to the database")
    
    def clear_all(self, *args , **kwargs):
        #clear the entry fields
        self.roll_e.delete(0 , tkinter.END)
        self.name_e.delete(0 , tkinter.END)
        self.sub_e.delete(0 , tkinter.END)
        self.phone_e.delete(0 , tkinter.END)

  
# creating the object
root = tkinter.Tk()
b = Database(root)

root.geometry("1200x720+0+0")
root.title("Faculty Registration")
root.mainloop()