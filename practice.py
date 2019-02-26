from tkinter import *

a = Tk()

a.title("convert")
def j():
    h=int(c.get())
    mr=h*1000
    ml=h*2.20462
    p=h*35.274
    e2.insert(END,mr)
    e3.insert(END,ml)
    e4.insert(END,p)


b1=Button(a,text="convert",command=j)
b1.grid(row=0,column=2)
c=StringVar()
e1=Entry(a,textvariable=c)
e1.grid(row=0,column=1)
e2=Text(a,height=1,width=20)
e2.grid(row=1,column=0)
e3=Text(a,height=1,width=20)
e3.grid(row=1,column=1)
e4=Text(a,height=1,width=20)
e4.grid(row=1,column=2)

t1=Label(a,text="kg",height=1,width=20)
t1.grid(row=0,column=0)


a.mainloop()
