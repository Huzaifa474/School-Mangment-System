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
def Registration():
    win.withdraw()
    labelfont3=('times',20,'bold')
    a=email_var.get() #name of student
    b=name_var.get()#fathername of student
    c=Add_var.get()#email
    d=Qual_var.get()#date of birth
    e=pass_var.get()# contract number
    cursor=con.cursor()
    cursor.execute("INSERT INTO Teacher(tid,Tname,TAddress,TQaulification,Password) VALUES (?,?,?,?,?)",(a,b,c,d,e))
    con.commit()
    messagebox.showinfo("information","DATA ADDED")
win=tk.Tk()
win.title("Teacher Managment")
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
teacher_man=ttk.Label(win,text="\n\nTeacher Registration\n")
teacher_man.pack()
teacher_man.configure(background="grey")
teacher_man.config(font=labelfont1)
lab1=ttk.Label(win,text="Email")
lab1.pack()
lab1.configure(background="grey")
lab1.config(font=labelfont2)
email_var=tk.StringVar()
email_ent=ttk.Entry(win,width=30,textvariable=email_var)
email_ent.pack()
email_ent.config(font=labelfont1)
lab2=ttk.Label(win,text="Name")
lab2.pack()
lab2.configure(background="grey")
lab2.config(font=labelfont2)
name_var=tk.StringVar()
name_ent=ttk.Entry(win,width=30,textvariable=name_var)
name_ent.pack()
name_ent.config(font=labelfont1)
lab3=ttk.Label(win,text="Address")
lab3.pack()
lab3.configure(background="grey")
lab3.config(font=labelfont2)
Add_var=tk.StringVar()
Add_ent=ttk.Entry(win,width=30,textvariable=Add_var)
Add_ent.pack()
Add_ent.config(font=labelfont1)
lab4=ttk.Label(win,text="Qualification")
lab4.pack()
lab4.configure(background="grey")
lab4.config(font=labelfont2)
Qual_var=tk.StringVar()
Qual_ent=ttk.Entry(win,width=30,textvariable=Qual_var)
Qual_ent.pack()
Qual_ent.config(font=labelfont1)
lab5=ttk.Label(win,text="Password")
lab5.pack()
lab5.configure(background="grey")
lab5.config(font=labelfont2)
pass_var=tk.StringVar()
pass_ent=ttk.Entry(win,width=30,show=".",textvariable=pass_var)
pass_ent.pack()
pass_ent.config(font=labelfont1)
myFont = font.Font(size=15)
sub_butt=Button(win,text="Register",command=Registration)
sub_butt['font'] = myFont
sub_butt.pack(pady=10)
sub_butt.configure(width="20") 
win.mainloop()
