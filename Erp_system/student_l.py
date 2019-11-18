import tkinter 
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("F:/tArUN/programs/Python programs/erpsystem/Erp_system/Database/erp.db")
c = conn.cursor()

class Database:
    def __init__(self , master , *args , **kwargs):

        self.master= master
        # heading label
        self.heading = tkinter.Label(master, text="Student Information",  fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=300, y=0)
        
        #labels 
        self.search_l = tkinter.Label(master, text="Enter Student's Roll Number ", font=('arial 18 bold'))
        self.search_l.place(x=0, y=100)

        self.roll_l = tkinter.Label(master, text=" Roll Number", font=('arial 18 bold'))
        self.roll_l.place(x=0, y=200)

        self.name_l = tkinter.Label(master, text=" Name", font=('arial 18 bold'))
        self.name_l.place(x=0, y=300)

        self.course_l = tkinter.Label(master, text=" Course", font=('arial 18 bold'))
        self.course_l.place(x=0, y=400)

        self.branch_l = tkinter.Label(master, text=" Branch", font=('arial 18 bold'))
        self.branch_l.place(x=0, y=500)

        self.attend_l = tkinter.Label(master, text=" Attendance", font=('arial 18 bold'))
        self.attend_l.place(x=0, y=600)

        #entries for labels
        self.search_e = tkinter.Entry(master, width=15, font=('arial 18 bold'))
        self.search_e.place(x=380 , y=100)

        self.roll_e = tkinter.Entry(master, width=30, font=('arial 18 bold'))
        self.roll_e.place(x=200 , y=200)

        self.name_e = tkinter.Entry(master, width=30, font=('arial 18 bold'))
        self.name_e.place(x=200 , y=300)

        self.course_e = tkinter.Entry(master, width=30, font=('arial 18 bold'))
        self.course_e.place(x=200 , y=400)

        self.branch_e = tkinter.Entry(master, width=30, font=('arial 18 bold'))
        self.branch_e.place(x=200 , y=500)

        self.attend_e = tkinter.Entry(master, width=30, font=('arial 18 bold'))
        self.attend_e.place(x=200 , y=600)

         #search db button
        self.btn_search = tkinter.Button(master, text="Search", width=20, height=2, bg='steelblue', command = self.search)
        self.btn_search.place(x=600, y=100)

    def search(self, *args, **kwargs):
        sql = "SELECT * FROM student WHERE id=?"
        result = c.execute(sql, (self.search_e.get(), ))
        for r in result:
            self.n1 = r[0] #roll
            self.n2 = r[1] #name
            self.n3 = r[2] #branch
            self.n4 = r[3] #course
            self.n5 = r[4] #attendance
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

        self.course_e.config(state='normal')
        self.course_e.delete(0, tkinter.END)
        self.course_e.insert(0, str(self.n3))
        self.course_e.config(state='readonly')

        self.branch_e.config(state='normal')
        self.branch_e.delete(0, tkinter.END)
        self.branch_e.insert(0, str(self.n4))
        self.branch_e.config(state='readonly')

        self.attend_e.config(state='normal')
        self.attend_e.delete(0, tkinter.END)
        self.attend_e.insert(0, str(self.n5))
        self.attend_e.config(state='readonly')

  
# creating the object
root = tkinter.Tk()
b = Database(root)

root.geometry("1200x720+0+0")
root.title("Student Information")
root.mainloop()