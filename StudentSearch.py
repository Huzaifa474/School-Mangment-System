import pyodbc
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
con=pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-5E0N47M\SQLEXPRESS;"
    "Database=School Managment System;"
    "Trusted_Connnection=yes;"
)
def search():
    win.withdraw()
    a=sear_var.get()
    cursor=con.cursor()
    cursor.execute("select * from student where Rollno=?",a)
    ans=cursor.fetchall()
    con.commit()    
    for i in ans:
        win1=tk.Tk()
        win1.title("Teacher Managment")
        win1.geometry("800x400")
        win1.configure(background="grey")
        labelfont=('times',20,'bold')
        labelfont1=('times',15,'bold')
        labelfont2=('times',18,'bold')
        head=ttk.Label(win1,text="\n\tSCHOOL MANAGEMENT SYSTEM\t\n")
        head.pack()
        head.configure(background="blue",width="200")
        head.config(font=labelfont2)
        res_man=ttk.Label(win1,text=i)
        res_man.pack()
        res_man.configure(background="grey")
        res_man.config(font=labelfont1)
        win1.mainloop()
        
    
win=tk.Tk()
win.title("Student Managment")
win.geometry("700x400")
win.resizable(0, 0)
win.configure(background="grey")
labelfont=('times',20,'bold')
labelfont1=('times',15,'bold')
labelfont2=('times',18,'bold')
head=ttk.Label(win,text="\n\tSCHOOL MANAGEMENT SYSTEM\t\n")
head.pack()
head.configure(background="blue",width="200")
head.config(font=labelfont2)
teacher_man=ttk.Label(win,text="\n\nSearch")
teacher_man.pack()
teacher_man.configure(background="grey")
teacher_man.config(font=labelfont1)
sear_var=tk.StringVar()
email_ent=ttk.Entry(win,width=30,textvariable=sear_var)
email_ent.pack()
email_ent.config(font=labelfont1)
myFont = font.Font(size=15)
sub_butt=Button(win,text="SEARCH",command=search)
sub_butt['font'] = myFont
sub_butt.pack(pady=10)
sub_butt.configure(width="10")
win.mainloop()