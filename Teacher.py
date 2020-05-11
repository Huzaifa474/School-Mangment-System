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

def Register():
    win.withdraw()
    import TeacherReg
def Search():
    win.withdraw()
    import Search
def Courses():
    win.withdraw()
    import courses
win=Tk()
win.title("Teacher Managment")
win.geometry("600x500")
win.resizable(0, 0)
win.configure(background="grey")
labelfont=('times',20,'bold')
labelfont1=('times',15,'bold')
labelfont2=('times',18,'bold')
head=ttk.Label(win,text="\n\tSCHOOL MANAGEMENT SYSTEM\t\n")
head.pack()
head.configure(background="blue",width="200")
head.config(font=labelfont2)
teacher_man=ttk.Label(win,text="\n\nTeacher Managment\n")
teacher_man.pack()
teacher_man.configure(background="grey")
teacher_man.config(font=labelfont1)
head1=ttk.Label(win,text="Register")
head1.pack()
head1.configure(background="grey")
head1.config(font=labelfont1)
myFont = font.Font(size=15)
reg_butt=Button(win,text="Register",command=Register)
reg_butt['font'] = myFont
reg_butt.pack(pady=10)
reg_butt.configure(width="20")
head2=ttk.Label(win,text="search")
head2.pack()
head2.configure(background="grey")
head2.config(font=labelfont1)
sear_butt=Button(win,text="search",command=Search)
sear_butt['font'] = myFont
sear_butt.pack(pady=10)
sear_butt.configure(width="20")
head3=ttk.Label(win,text="Courses")
head3.pack()
head3.configure(background="grey")
head3.config(font=labelfont1)
Cour_butt=Button(win,text="Courses",command=Courses)
Cour_butt['font'] = myFont
Cour_butt.pack(pady=10)
Cour_butt.configure(width="20") 
win.mainloop()