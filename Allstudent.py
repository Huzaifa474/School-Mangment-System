import pyodbc
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import os
con=pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-5E0N47M\SQLEXPRESS;"
    "Database=School Managment System;"
    "Trusted_Connnection=yes;"
)
def search():
    win.withdraw()
    cursor=con.cursor()
    cursor.execute("select * from student")
    codepath="C:\\Users\\Admin\\Documents\\Alldata.txt"
    os.startfile(codepath)
    for row in cursor.fetchall():
        print(row)

def Class():
    a=new_var.get()
    cursor=con.cursor()
    cursor.execute("select * from student where class=?",a)
    for res in cursor.fetchall():
        print(res)
    
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
head1=ttk.Label(win,text="\n\tStudent Managment\t\n")
head1.pack()
head1.configure(background="grey")
head1.config(font=labelfont2)
myFont = font.Font(size=15)
sub_butt=Button(win,text="All RECORD",command=search)
sub_butt['font'] = myFont
sub_butt.pack(pady=10)
sub_butt.configure(width="10")
new_var=tk.StringVar()
name_ent=ttk.Entry(win,width=30,textvariable=new_var)
name_ent.pack()
name_ent.config(font=labelfont1)
sub_butt1=Button(win,text="SEE BY CLASS",command=Class)
sub_butt1['font'] = myFont
sub_butt1.pack(pady=10)
sub_butt1.configure(width="15")
win.mainloop()
