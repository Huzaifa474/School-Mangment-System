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
def sheet():
    win.withdraw()
    import marksheet
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
head1=ttk.Label(win,text="Marks Managment")
head1.pack()
head1.configure(background="grey")
head1.config(font=labelfont1)
myFont = font.Font(size=15)
reg_butt=Button(win,text="Marks Mangment",command=sheet)
reg_butt['font'] = myFont
reg_butt.pack(pady=10)
reg_butt.configure(width="20")
win.mainloop()