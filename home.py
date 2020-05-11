import pyodbc
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from turtle import *
def splashscreen():
    t = Turtle()
    t.speed(10)
    t.hideturtle()
    t.write("SCHOOL MANAGMENT SYSTEM", move=True, align="CENTER",
            font=("Agency FB", 30, "bold", "underline"))
    t.goto(-200, 0)
    t.penup()
    t.goto(-200, 10)
    t.bk(70)
    t.pendown()
    for i in range(20):
        t.pensize(2)
        t.fd(60)
        t.lt(90)
        t.left(10)
def Login():
    win.withdraw()
    import login
def AdLogin():
    win.withdraw()
    import Admin
splashscreen()
win=Tk()
win.title("Home Page")
win.geometry("600x400")
win.resizable(0, 0)
win.configure(background="grey")
labelfont=('times',20,'bold')
labelfont1=('times',15,'bold')
labelfont2=('times',18,'bold')
head=ttk.Label(win,text="\n\tSCHOOL MANAGEMENT SYSTEM\t\n")
head.pack()
head.configure(background="blue",width="200")
head.config(font=labelfont2)
head1=ttk.Label(win,text="\nHOME PAGE\n")
head1.pack()
head1.configure(background="grey")
head1.config(font=labelfont2)
head2=ttk.Label(win,text="LOGIN")
head2.pack()
head2.configure(background="grey")
head2.config(font=labelfont1)
myFont = font.Font(size=25)
reg_butt=Button(win,text="LOGIN",command=Login)
reg_butt['font'] = myFont
reg_butt.pack(pady=10)
reg_butt.configure(width="25")
head2=ttk.Label(win,text="LOGIN AS ADMIN")
head2.pack()
head2.configure(background="grey")
head2.config(font=labelfont1)
reg_butt=Button(win,text="ADMIN LOGIN",command=AdLogin)
reg_butt['font'] = myFont
reg_butt.pack(pady=10)
reg_butt.configure(width="25")
win.mainloop()
