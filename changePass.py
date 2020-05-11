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
def ChangePass():
    labelfont3=('times',20,'bold')
    a=old_var.get() #name of student
    b=new_var.get()#fathername of student
    cursor=con.cursor()
    cursor.execute("update Adlogin set Adpass=? where Adpass=?",(b,a))
    con.commit()
    messagebox.showinfo("information","Password Updated")
win1=Tk()
win1.title("Admin Managment")
win1.geometry("600x400")
win1.resizable(0, 0)
win1.configure(background="grey")
labelfont=('times',20,'bold')
labelfont1=('times',15,'bold')
labelfont2=('times',18,'bold')
head=ttk.Label(win1,text="\n\tSCHOOL MANAGEMENT SYSTEM\t\n")
head.pack()
head.configure(background="blue",width="200")
head.config(font=labelfont2)
myFont = font.Font(size=15)
lab1=ttk.Label(win1,text="Old Password:")
lab1.pack()
lab1.configure(background="grey")
lab1.config(font=labelfont2)
old_var=tk.StringVar()
corus_ent=ttk.Entry(win1,width=30,show="*",textvariable=old_var)
corus_ent.pack()
corus_ent.config(font=labelfont1)
lab2=ttk.Label(win1,text="New Password")
lab2.pack()
lab2.configure(background="grey")
lab2.config(font=labelfont2)
new_var=tk.StringVar()
name_ent=ttk.Entry(win1,width=30,show="*",textvariable=new_var)
name_ent.pack()
name_ent.config(font=labelfont1)
sub_butt=Button(win1,text="\nChange Password",command=ChangePass)
sub_butt['font'] = myFont
sub_butt.pack(pady=10)
sub_butt.configure(width="15")
win1.mainloop()