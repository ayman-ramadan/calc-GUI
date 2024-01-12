from tkinter import *
from tkinter import messagebox
import math
root = Tk()

x=''
y=''
c=''
def add_num(num):
    global c
    global x
    global y
    if e.get()=="division on zero!":
        e.delete(0,END)
    if c=='' and not y=='':
        clear()
    e.insert(END,num)
def clear():
    global x
    global y
    global c
    e.delete(0,END)
    x=''
    y=''
    c=''
def operation(cc):
    global y
    global c
    if cc == 'sin' or cc == 'cos' or cc == 'tan':
        pass
    else:
        y=float(e.get() if not (e.get()=='') else y)
    e.delete(0,END)
    c=cc
def equal():
    global c
    global x
    global y
    global e
    x=float(e.get())
    e.delete(0,END)
    
    if (x=='' or y=='' or c=='') and not( c=='sin'or c =='cos'or c =='tan'):
        clear()
    elif c=='+':
        e.insert(0,y+x)
    elif c =='-':
        e.insert(0,y-x)
    elif c=='*':
        e.insert(0,y*x)
    elif c=='/':
        if x==0:
            clear()
            messagebox.showerror("Error","division on zero is not aplicabel!")
        else:
            e.insert(0,y/x)
    elif c=='^':
        e.insert(0,y**x)
    elif c == 'sin':
        e.insert(0,math.sin(x))
    elif c == 'cos':
        e.insert(0,math.cos(x))
    elif c == 'tan':
        e.insert(0,math.tan(x))
    elif c=='sqr':
        if x<0:
            clear()
            messagebox.showerror("Error","division on zero is not aplicabel!")
        else:
            e.insert(0,math.sqrt(x))
    else:
        pass
    c=''

root.title('calculator')
e=Entry(root,width=30,borderwidth=3,font=('arial',15))
but1=Button(root,padx=40,pady=20,command=lambda:add_num(1),text='1')
but2=Button(root,padx=40,pady=20,command=lambda:add_num(2),text='2')
but3=Button(root,padx=40,pady=20,command=lambda:add_num(3),text='3')
but4=Button(root,padx=40,pady=20,command=lambda:add_num(4),text='4')
but5=Button(root,padx=40,pady=20,command=lambda:add_num(5),text='5')
but6=Button(root,padx=40,pady=20,command=lambda:add_num(6),text='6')
but7=Button(root,padx=40,pady=20,command=lambda:add_num(7),text='7')
but8=Button(root,padx=40,pady=20,command=lambda:add_num(8),text='8')
but9=Button(root,padx=40,pady=20,command=lambda:add_num(9),text='9')
but0=Button(root,padx=40,pady=20,command=lambda:add_num(0),text='0')
butc=Button(root,padx=76,pady=19,command=clear,text='clear',font=('arial',10))
but_Plus=Button(root,padx=34,pady=14,command=lambda:operation('+'),text='+',font=('arial',15))
but_minus=Button(root,padx=37,pady=14,command=lambda:operation('-'),text='-',font=('arial',15))
but_multiplication=Button(root,padx=35,pady=14,command=lambda:operation('*'),text='*',font=('arial',15))
but_division=Button(root,padx=37,pady=14,command=lambda:operation('/'),text='/',font=('arial',15))
but_sin=Button(root,padx=27,pady=14,command=lambda:operation('sin'),text='sin',font=('arial',15))
but_cos=Button(root,padx=23,pady=14,command=lambda:operation('cos'),text='cos',font=('arial',15))
but_tan=Button(root,padx=25,pady=14,command=lambda:operation('tan'),text='tan',font=('arial',15))
but_sqr=Button(root,padx=22,pady=14,command=lambda:operation('sqr'),text='sqrt',font=('arial',15))
but_pow=Button(root,padx=35,pady=14,command=lambda:operation('^'),text='^',font=('arial',15))
buteq=Button(root,padx=82,pady=14,command=equal,text='=',font=('arial',15))

e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
but1.grid(row=1,column=0)
but2.grid(row=1,column=1)
but3.grid(row=1,column=2)
but4.grid(row=2,column=0)
but5.grid(row=2,column=1)
but6.grid(row=2,column=2)
but7.grid(row=3,column=0)
but8.grid(row=3,column=1)
but9.grid(row=3,column=2)
but0.grid(row=4,column=0)
butc.grid(row=4,column=1,columnspan=2)
but_Plus.grid(row=5,column=0)
but_minus.grid(row=5,column=1)
but_multiplication.grid(row=5,column=2)
but_division.grid(row=6,column=0)
but_sin.grid(row=1,column=3)
but_cos.grid(row=2,column=3)
but_tan.grid(row=3,column=3)
but_sqr.grid(row=4,column=3)
but_pow.grid(row=5,column=3)
buteq.grid(row=6,column=1,columnspan=2)

root.mainloop()