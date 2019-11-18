import tkinter 
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("F:/tArUN/programs/Python programs/erpsystem/Erp_system/Database/erp.db")
c = conn.cursor()

class Database:
    def __init__(self , master , *args , **kwargs):

        self.master= master
        # heading label
        self.heading = tkinter.Label(master, text="Student Registration",  fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=450, y=0)
        
        #labels 
        self.roll_l = tkinter.Label(master, text="Enter Student's Roll Number", font=('arial 18 bold'))
        self.roll_l.place(x=0, y=100)

        self.name_l = tkinter.Label(master, text="Enter Student's Name", font=('arial 18 bold'))
        self.name_l.place(x=0, y=200)

        self.course_l = tkinter.Label(master, text="Enter Student's Course", font=('arial 18 bold'))
        self.course_l.place(x=0, y=300)

        self.branch_l = tkinter.Label(master, text="Enter Student's Branch", font=('arial 18 bold'))
        self.branch_l.place(x=0, y=400)

        self.attend_l = tkinter.Label(master, text="Enter Student's Attendance", font=('arial 18 bold'))
        self.attend_l.place(x=0, y=500)

        #entries for labels
        self.roll_e = tkinter.Entry(master, width=30, font=('arial 18 bold'))
        self.roll_e.place(x=380 , y=100)

        self.name_e = tkinter.Entry(master, width=30, font=('arial 18 bold'))
        self.name_e.place(x=380 , y=200)

        self.course_e = tkinter.Entry(master, width=30, font=('arial 18 bold'))
        self.course_e.place(x=380 , y=300)

        self.branch_e = tkinter.Entry(master, width=30, font=('arial 18 bold'))
        self.branch_e.place(x=380 , y=400)

        self.attend_e = tkinter.Entry(master, width=30, font=('arial 18 bold'))
        self.attend_e.place(x=380 , y=500)

         # add to db button
        self.btn_add = tkinter.Button(master, text="ADD", width=20, height=2, bg='steelblue', command = self.write_stu)
        self.btn_add.place(x=585, y=550)

         # clear field button
        self.btn_clr = tkinter.Button(master, text="CLEAR", width=20, height=2, bg='steelblue', command = self.clear_all)
        self.btn_clr.place(x=400, y=550)

        # text box for logs
        self.tBox = tkinter.Text(master , width = 60, height = 27)
        self.tBox.place(x=850 ,  y= 100)
    
    def write_stu(self , *args , **kwargs):
        #get from entries
        self.roll = self.roll_e.get()
        self.name = self.name_e.get()      
        self.course = self.course_e.get()
        self.branch = self.branch_e.get()
        self.attend = self.attend_e.get()

        if self.name == '' or  self.roll == '' or self.course == '' or self.branch == '' or self.attend == '' :
            tkinter.messagebox.showwarning("Warning" , "PLEASE FILL ALL THE ENTRIES")
        else:
            
            sql = "INSERT INTO student ( id , name , course , branch , attendance ) VALUES(?,?,?,?,?)"
            c.execute(sql , (self.roll , self.name , self.course , self.branch , self.attend))
            conn.commit()
            #text box msg
            self.tBox.insert(tkinter.END, "\n\n Inserted " + str(self.name) + " into the database\n with roll id = " + str(self.roll_e.get()))

            tkinter.messagebox.showinfo("Success" , "Successfully added to the database")
    
    def clear_all(self, *args , **kwargs):
        #clear the entry fields
        self.roll_e.delete(0 , tkinter.END)
        self.name_e.delete(0 , tkinter.END)
        self.course_e.delete(0 , tkinter.END)
        self.branch_e.delete(0 , tkinter.END)
        self.attend_e.delete(0 , tkinter.END)


  
# creating the object
root = tkinter.Tk()
b = Database(root)

root.geometry("1200x720+0+0")
root.title("Student Registration")
root.mainloop()