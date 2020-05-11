import pyodbc
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
con=pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-5E0N47M\SQLEXPRESS;"
    "Database=School Managment System;"
    "Trusted_Connnection=yes;"
)
def Logout():
    import Admin
#cursor=con.cursor()
win=tk.Tk()
def AdminLogin():
    win.withdraw()
    username=Ad_var.get()
    Pass=Adpass_var.get()
    if len(username)==0 and len(Pass)==0:
        messagebox.showerror("EEROR","KINDLY FILL THE FEILDS")    
        import Admin
    elif username=="huzaifa" and Pass=="123456" or username=="Hasaan" and Pass=="123456":
        cursor=con.cursor()
        cursor.execute("SELECT * from Adlogin Where Adpass=?",Pass)
        run = cursor.fetchall()
        con.commit()
        #if run==True:
        win1=tk.Tk()
        win1.resizable(0, 0)
        labelfont4=('times',18,'bold')
        win1.geometry("600x500")
        win1.title(username)
        win1.configure(background="grey")
        heading=ttk.Label(win1,text="SCHOOL MANAGMENT SYSTEM")
        heading.pack()
        heading.configure(background="blue",width="200")
        heading.config(font=labelfont4)
        mess=ttk.Label(win1,text="WELCOME")
        mess.pack()
        mess.config(font=labelfont4)
        mess.configure(background="grey")
        head=ttk.Label(win1,text="\nAdmin name:")
        head.pack()
        head.configure(background="grey")
        head.config(font=labelfont4)
        nam=ttk.Label(win1,text=username)
        nam.pack()
        nam.configure(background="grey",foreground="white")
        nam.config(font=labelfont4)
        fun=ttk.Label(win1,text="ADMIN FUNCTIONS\n")
        fun.pack()
        fun.config(font=labelfont4)
        fun.configure(background="grey")
        fun1=ttk.Label(win1,text="Student Details")
        fun1.pack()
        fun1.config(font=labelfont4)
        fun1.configure(background="grey")
        fun1_butt=ttk.Button(win1,text="STUDENTS DETIALS",command=addStudent)
        fun1_butt.pack(pady=5)
        fun1_butt.configure(width="30")
        fun1_butt.config()
        fun2=ttk.Label(win1,text="ADMIN DETAILS")
        fun2.pack()
        fun2.config(font=labelfont4)
        fun2.configure(background="grey")
        fun2_butt=ttk.Button(win1,text="change Password",command=AdminDetails)
        fun2_butt.pack(pady=5)
        fun2_butt.configure(width="30")
        fun2_butt.config()
        fun3=ttk.Label(win1,text="TEACHERS DETAILS")
        fun3.pack()
        fun3.config(font=labelfont4)
        fun3.configure(background="grey")
        fun3_butt=ttk.Button(win1,text="Teacher Details",command=addTeacher)
        fun3_butt.pack()
        fun3_butt.configure(width="30")
        fun4=ttk.Label(win1,text="MANAGMENT DETAILS")
        fun4.pack()
        fun4.config(font=labelfont4)
        fun4.configure(background="grey")
        fun4_butt=ttk.Button(win1,text="Managment Details",command=managment)
        fun4_butt.pack()
        fun4_butt.configure(width="30")
        logout=ttk.Button(win1,text="LOGOUT",command=win1.destroy)
        logout.pack(pady=20)
        logout.configure(width="20")
        win1.mainloop()
    else:
        a=0
        while(a<3):
            win.withdraw()
            win1=tk.Tk()
            win1.withdraw()
            messagebox.showerror("ERROR","INVALID USERNAME OR PASSWORD")
            import Admin
            a+= 1
            if a==3:
                messagebox.showerror("ERROR","TRY AGAIN IN FEW SECONDS")
                break
    import Admin
def addStudent():
    import Student
def AdminDetails():
    import Admindet   
def addTeacher():
    import Teacher
    win1=tk.Tk()
    win1.withdraw()
def managment():
    import managment

   
win.title("Admin Login")
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
log=ttk.Label(win,text="\n\nADMIN LOGIN")
log.pack()
log.configure(background="grey")
log.config(font=labelfont1)
Adname=ttk.Label(win,text="\n\nAdmin ID")
Adname.pack()
Adname.configure(background="grey")
Adname.config(font=labelfont1)
Ad_var=tk.StringVar()
Ad_ent=ttk.Entry(win,width=30,textvariable=Ad_var)
Ad_ent.pack()
Ad_ent.config(font=labelfont1)
Adpass=ttk.Label(win,text="\nAdmin Password")
Adpass.pack()
Adpass.configure(background="grey")
Adpass.config(font=labelfont1)
Adpass_var=tk.StringVar()
Ad_pass=ttk.Entry(win,width="30",show="*",textvariable=Adpass_var)
Ad_pass.pack()
Ad_pass.configure(background="grey")
Ad_pass.config(font=labelfont1)
sub_but=ttk.Button(win,text="LOGIN",command=AdminLogin)
sub_but.pack(pady=15)
sub_but.configure(width="20")
win.mainloop()