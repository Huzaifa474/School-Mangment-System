import tkinter as tk
from tkinter import ttk
import pyodbc
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
def Register1():
    import StuReg
def Search():
    import StudentSearch
def Marksheet():
    import marksheet
def changePassword():
    import updatePass
def LogRes():
    win.withdraw()
    labelfont3=('times',20,'bold')
    a=sear_var.get() #name of student
    b=pass_var.get()#fathername of student
    cursor=con.cursor()
    cursor.execute("select Tname from Teacher where Password=?",b)
    ans=cursor.fetchall()
    for i in ans:
        win1=tk.Tk()
        win1.title("Teacher Managment")
        win1.geometry("800x600")
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
        res1_man=ttk.Label(win1,text="Register Student")
        res1_man.pack()
        res1_man.configure(background="grey")
        res1_man.config(font=labelfont1)
        myFont = font.Font(size=15)
        sub_butt2=tk.Button(win1,text="Register",command=Register1)
        sub_butt2['font'] = myFont
        sub_butt2.pack(pady=10)
        sub_butt2.configure(width="10")
        res2_man=ttk.Label(win1,text="Search Student")
        res2_man.pack()
        res2_man.configure(background="grey")
        res2_man.config(font=labelfont1)
        myFont = font.Font(size=15)
        sub_butt3=tk.Button(win1,text="Search",command=Search)
        sub_butt3['font'] = myFont
        sub_butt3.pack(pady=10)
        sub_butt3.configure(width="10")
        res4_man=ttk.Label(win1,text="Generate Marksheet")
        res4_man.pack()
        res4_man.configure(background="grey")
        res4_man.config(font=labelfont1)
        myFont = font.Font(size=15)
        sub_butt3=tk.Button(win1,text="Generate Marksheet",command=Marksheet)
        sub_butt3['font'] = myFont
        sub_butt3.pack(pady=10)
        sub_butt3.configure(width="20")
        res1_man=ttk.Label(win1,text="Change Password")
        res1_man.pack()
        res1_man.configure(background="grey")
        res1_man.config(font=labelfont1)
        myFont = font.Font(size=15)
        sub_butt2=tk.Button(win1,text="Change Password",command=changePassword)
        sub_butt2['font'] = myFont
        sub_butt2.pack(pady=10)
        sub_butt2.configure(width="20")
        win1.mainloop()
   
win=tk.Tk()
win.title("Student Managment")
win.geometry("700x500")
win.resizable(0, 0)
win.configure(background="grey")
labelfont=('times',20,'bold')
labelfont1=('times',15,'bold')
labelfont2=('times',18,'bold')
head=ttk.Label(win,text="\n\tSCHOOL MANAGEMENT SYSTEM\t\n")
head.pack()
head.configure(background="blue",width="200")
head.config(font=labelfont2)
teacher_man=ttk.Label(win,text="\n\nUsername")
teacher_man.pack()
teacher_man.configure(background="grey")
teacher_man.config(font=labelfont1)
sear_var=tk.StringVar()
email_ent=ttk.Entry(win,width=30,textvariable=sear_var)
email_ent.pack()
email_ent.config(font=labelfont1)
myFont = font.Font(size=15)
teacher1_man=ttk.Label(win,text="\nPassword")
teacher1_man.pack()
teacher1_man.configure(background="grey")
teacher1_man.config(font=labelfont1)
pass_var=tk.StringVar()
pass_ent=ttk.Entry(win,show="*",width=30,textvariable=pass_var)
pass_ent.pack()
pass_ent.config(font=labelfont1)
sub_butt=tk.Button(win,text="LOGIN",command=LogRes)
sub_butt['font'] = myFont
sub_butt.pack(pady=10)
sub_butt.configure(width="10")
teacher2_man=ttk.Label(win,text="\n\nREGISTER HERE")
teacher2_man.pack()
teacher2_man.configure(background="grey")
teacher2_man.config(font=labelfont1)
sub_butt1=tk.Button(win,text="Register",command=Register)
sub_butt1['font'] = myFont
sub_butt1.pack(pady=10)
sub_butt1.configure(width="10")
win.mainloop()