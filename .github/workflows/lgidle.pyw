from sqlite3.dbapi2 import Date
from tkinter import*
from tkinter import Entry
from tkinter import messagebox
from tkinter.font import BOLD
from typing import Tuple
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
import sqlite3
import time
from datetime import datetime
from tkcalendar import *
from tkcalendar import DateEntry


#----root window
root=tk.Tk()
root.title("Expenditure Monitor")
root.geometry("1200x700+200+70")
root.resizable(False,False)
img = PhotoImage("aas.jpg")
canvas=Canvas(root,width=1200, height=700)
im=ImageTk.PhotoImage(Image.open("aas.jpg")) 
canvas.create_image(0,0,anchor=NW,image=im)
canvas.pack()

s= ttk.Style()
s.theme_use('clam')
strdisp=tk.StringVar(root)

#----frame declaration
framei=tk.Frame(root)
frame1=tk.Frame(root)
frame2=tk.Frame(root)
frame3=tk.Frame(root)

#----global variables
date_entry = StringVar()
expen = StringVar()
descrip = StringVar()
date_fetch = StringVar()
drow = tuple()
mrow = tuple()
entry1=StringVar()
entry2=StringVar()
month_entry = StringVar()


#----frame in root window

framei=tk.Frame(root,bg='skyblue')
framei.place(x=835,y=170, width=370, height=380)
Label(root,text="Username",font=("Times",17),bg='skyblue',bd=5).place(x=850,y=280)
Label(root,text="Password",font=("Times",17),bg='skyblue',bd=5).place(x=850,y=380)

entry1=Entry(root,bd=5,font=("Times",15))
entry1.place(x=980,y=275,height=50)

entry2=Entry(root,bd=5,show="*",font=("Times",15))
entry2.place(x=980,y=375,height=50)
b1=Button(root,text="Login",command=lambda:login(),height=2,width=13,bd=5,font=("Times",16)).place(x=900,y=450)





def close():
    root.destroy()


def frames(frame):

    #----frame1
    frame1.place(width=1200, height=900)
    image1 = Image.open("key.jpg")
    photo1 = ImageTk.PhotoImage(image1.resize((1200,900)))
    label1=Label(frame1,image=photo1)
    label1.image = photo1
    label1.pack()
   
    Label(frame1,text="Welcome Francis !",bg='black',font=("Times",18),fg='orange',relief="raised",bd=5).place(x=550,y=275)
    Button(frame1,text="Entry",command=lambda:show_frame(frame2),height=2,width=13,bd=5,font=("Times",15),bg='black',fg='light green').place(x=220,y=555)
    Button(frame1,text="Exit",command=lambda:close(),height=2,width=13,bd=5,font=("Times",15),bg='black',fg='orange').place(x=550,y=552)
    Button(frame1,text="Fetch",command=lambda:show_frame(frame3),height=2,width=13,bd=5,font=("Times",15),bg='black',fg='light green').place(x=880,y=548)
    
    

    #----frame2

    frame2.place(width=1200, height=900)
    image2 = Image.open("chess.jpg")
    photo2 = ImageTk.PhotoImage(image2.resize((1200,900)))
    label2=Label(frame2,image=photo2)
    label2.image = photo2
    label2.pack()
    
    Label(frame2,text="Date",font=("Times",17),bg='#757575',bd=5,relief="groove").place(x=400,y=45)
    Label(frame2,text="Expense",font=("Times",17),bg='#7b7a7b',bd=5,relief="groove").place(x=400,y=130)
    entry2=Entry(frame2,bd=5,font=("Times",15),textvariable=expen)
    entry2.place(x=590,y=123,height=50)
    
    Label(frame2,text="Description",font=("Times",17),bg='#737373',bd=5,relief="groove").place(x=400,y=210)
    entry3=Entry(frame2,bd=5,font=("Times",15),textvariable=descrip)
    entry3.place(x=590,y=203,height=50)

    Label(frame2,text="Month",font=("Times",17),bg='#737373',bd=5,relief="groove").place(x=850,y=45)
    entry4 = ttk.Combobox(frame2,font=("Times",15),textvariable=month_entry) 
    entry4['values'] = ['Januvary','February','March','April','May','June','July','August','September','October','November','December']
    entry4.place(x=960,y=43,height=45)
    
    chekbox = IntVar()
    Checkbutton(frame2, text='Today',bg='black', fg='white' ,variable = chekbox, onvalue=1, offvalue=0, command=lambda:todaydate(),relief="groove").place(x=760,y=50)

    Button(frame2,text="Back",command=lambda:[show_frame(frame1),fr2deleteentry()],height=2,width=13,bd=5,font=("Times",15),bg='black',fg='light green').place(x=970,y=545)
    Button(frame2,text="Exit",command=lambda:close(),height=2,width=13,bd=5,font=("Times",15),bg='black',fg='orange').place(x=100,y=555)
    Button(frame2,text="Save",bg='black',height=2,width=13,bd=5,font=("Times",15),fg='sky blue',command=lambda:[sqlupdate(), fr2deleteentry()]).place(x=530,y=545)

    entrym1 = DateEntry(frame2,selectmode="day",bd=5,font=("Times",15),textvariable=date_entry,date_pattern='dd/mm/y')
    entrym1.place(x=590,y=43,height=50)
    
    def fr2deleteentry():
       
        entry2.delete(0, 'end')
        entry3.delete(0, 'end')
        entry4.delete(0, 'end')
    

    #----frame3
    frame3.place(width=1200, height=900)
    image3 = Image.open("flower.jpg")
    photo3 = ImageTk.PhotoImage(image3.resize((1200,900)))
    label3=Label(frame3,image=photo3)
    label3.image = photo3
    label3.pack()
    
    global dateentry
    global monthentry
    dateentry = DateEntry(frame3,bd=5,font=("Times",15),selectmode="day",date_pattern='dd/mm/y') 
    dateentry.place(x=120,y=300,width=130)
    Button(frame3,text="Date fetch",command=lambda:sqldatefetch(),height=2,width=13,bd=5,font=("Times",15),bg='black',fg='yellow').place(x=100,y=400)

    monthentry = ttk.Combobox(frame3,font=("Times",15)) 
    monthentry['values'] = ['Januvary','February','March','April','May','June','July','August','September','October','November','December']
    monthentry.place(x=980,y=290,width=130)

    Button(frame3,text="Month fetch",command=lambda:sqlmonfetch(),height=2,width=13,bd=5,font=("Times",15),bg='black',fg='yellow').place(x=960,y=395)
    Button(frame3,text="Exit",command=lambda:close(),height=2,width=13,bd=5,font=("Times",15),bg='black',fg='orange').place(x=100,y=600)
    Button(frame3,text="Back",command=lambda:[show_frame(frame1),fr3deleteentry()],height=2,width=13,bd=5,font=("Times",15),bg='black',fg='light green').place(x=960,y=600)

    def fr3deleteentry():
        monthentry.delete(0, 'end')


def login():

    username=entry1.get()
    password=entry2.get()

    if (username=="" and password==""):
        messagebox.showinfo("","Field is blank")
    elif(username=="francis" and password=="ultra1"):
        messagebox.showinfo("","Login Success")
        show_frame(frame1)
    else:
        messagebox.showinfo("","Incorrect Username or Password")


def log_dele():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')  


def show_frame(frame):
    frame.tkraise()
    if (frame == frame1):
        frames(frame1)
    elif (frame == frame2):
        frames(frame2)
    elif (frame == frame3):
        frames(frame3)

    # for loop getting delayed
    # for frame in (frame1,frame2,frame3):
    #     frames(frame)


def todaydate():
    tp1 = time.localtime()
    ftp1 = time.strftime("%d/%m/%Y",tp1)
    mtp = time.strftime("%B",tp1)
    date_entry.set(ftp1) 
    month_entry.set(mtp)


def sqlupdate():
    sqlcon=sqlite3.connect("database.db")
    c=sqlcon.cursor()
    c.execute("INSERT INTO extable VALUES('%s','%s','%s','%s')"%(date_entry.get(),expen.get(),descrip.get(),month_entry.get()) )
    sqlcon.commit()
    sqlcon.close()


def sqldatefetch():
    dattab = dateentry.get()
    global drow
    sqlcon=sqlite3.connect("database.db")
    c=sqlcon.cursor()
    query = """SELECT * FROM extable WHERE Date = :date """
    c.execute(query,{'date':dattab})
    drow = c.fetchall()
    treeviewdecide(drow)
    query1 = """SELECT SUM(Expenditure) FROM extable WHERE Date = :date """
    c.execute(query1,{'date':dattab})
    exdata=c.fetchall()
    #messagebox.showinfo("Total Expenditure in this Date",exdata)
    strdisp.set(exdata)
    Label(frame3,text="Total Amount Spent ",font=("Times",17),bg='black',relief="groove",bd=5,fg='skyblue').place(x=490,y=650)
    Label(frame3,textvariable=strdisp,font=("Times",17),bg='black',bd=5,relief="groove",fg='skyblue').place(x=720,y=650)
    sqlcon.commit()
    sqlcon.close()


def sqlmonfetch():
    global mrow
    montab = monthentry.get()
    sqlcon=sqlite3.connect("database.db")
    c=sqlcon.cursor()
    query= """SELECT * FROM extable WHERE Month = :month """
    c.execute(query,{'month':montab})
    mrow = c.fetchall()
    treeviewdecide(mrow)
    query1 = """SELECT SUM(Expenditure) FROM extable WHERE Month = :month """
    c.execute(query1,{'month':montab})
    modata=c.fetchall()
    strdisp.set(modata)
    Label(frame3,text="Total Amount Spent ",font=("Times",17),bg='black',relief="groove",bd=5,fg='skyblue').place(x=490,y=650)
    Label(frame3,textvariable=strdisp,font=("Times",17),bg='black',bd=5,relief="groove",fg='skyblue').place(x=720,y=650)
    #messagebox.showinfo("Total Expenditure in this Month is",modata)
    sqlcon.commit()
    sqlcon.close()


def treeviewdecide(r):
    
    def treeview(dec):
        s.configure('Treeview.Heading')
        trv_scroll = Scrollbar(frame3,orient=VERTICAL)
        trv=ttk.Treeview(frame3,columns=(1,2,3,4), show="headings",yscrollcommand=trv_scroll.set)    
        trv.place(x=300,y=80,height=500,bordermode=OUTSIDE)

        trv_scroll.config(command=trv.yview)
        trv_scroll.place(x=904,y=82,height=497,bordermode=OUTSIDE)
        trv.column(1,anchor=CENTER,width=120)
        trv.heading(1, text="Date")
        trv.column(2,anchor=CENTER,width=180)
        trv.heading(2, text="Expenditure")
        trv.column(3,anchor=CENTER,width=180)
        trv.heading(3, text="Description")
        trv.column(4,anchor=CENTER,width=120)
        trv.heading(4, text="Month")
        
        for i in dec:
            trv.insert('','end', values=i)

    
    if(r == drow):
        treeview(drow)
    elif(r == mrow):
        treeview(mrow)


root.mainloop()




