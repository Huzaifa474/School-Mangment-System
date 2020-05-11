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
    import StuReg
def Search():
    win.withdraw()
    import StudentSearch
def Courses():
    win.withdraw()
    import courses
def Record():
    win.withdraw()
    import Allstudent
win=Tk()
win.title("Student Managment")
win.geometry("600x600")
win.resizable(0, 0)
win.configure(background="grey")
labelfont=('times',20,'bold')
labelfont1=('times',15,'bold')
labelfont2=('times',18,'bold')
head=ttk.Label(win,text="\n\tSCHOOL MANAGEMENT SYSTEM\t\n")
head.pack()
head.configure(background="blue",width="200")
head.config(font=labelfont2)
teacher_man=ttk.Label(win,text="\n\nStudent Managment\n")
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
head3=ttk.Label(win,text="Delete")
head3.pack()
head3.configure(background="grey")
head3.config(font=labelfont1)
Cour_butt=Button(win,text="DELETE",command=Courses)
Cour_butt['font'] = myFont
Cour_butt.pack(pady=10)
Cour_butt.configure(width="20")
head4=ttk.Label(win,text="See all Students")
head4.pack()
head4.configure(background="grey")
head4.config(font=labelfont1)
all_butt=Button(win,text="SEE ALL STUDENTS",command=Record)
all_butt['font'] = myFont
all_butt.pack(pady=10)
all_butt.configure(width="20")  
win.mainloop()