from tkinter import *
def btnclick(santu):
    global yaahu
    yaahu=yaahu+str(santu)
    data.set(yaahu)

def btnclear():
    global yaahu
    yaahu=""
    data.set(yaahu)

def btneqaul():
    global yaahu
    equal=str(eval(yaahu))
    data.set(equal)


root=Tk()
root.title("GUI Of Calculater")
root.geometry("361x381+500+200")
yaahu=""
data=StringVar()
nameenty=Entry(root,textvariable=data,bd=29,bg="powder blue",justify="right",font=("ariel",20))
nameenty.grid(row=0,columnspan=4)

btn7=Button(root,text="7",font=("ariel",19,"bold"),bd=10,height=1,width=2,command=lambda :btnclick(7))
btn7.grid(row=1,column=0)
btn8=Button(root,text="8",font=("ariel",19,"bold"),bd=10,height=1,width=2,command=lambda :btnclick(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",font=("ariel",19,"bold"),bd=10,height=1,width=2,command=lambda :btnclick(9))
btn9.grid(row=1 ,column=2)
btnadd=Button(root,text="+",font=("ariel",19,"bold"),bd=10,height=1,width=2,command=lambda :btnclick("+"))
btnadd.grid(row=1 ,column=3)

btn4=Button(root,text="4",font=("airel",19,"bold"),bd=10,height=1,width=2,command=lambda :btnclick(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text="5",font=("airel",19,"bold"),bd=10,height=1,width=2,command=lambda :btnclick(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text="6",font=("airel",19,"bold"),bd=10,height=1,width=2,command=lambda :btnclick(6))
btn6.grid(row=2,column=2)
btnmul=Button(root,text="",font=("airel",19,"bold"),bd=10,height=1,width=2,command= lambda :btnclick(""))
btnmul.grid(row=2,column=3)

btn1=Button(root,text="1",font=("airel",19,"bold"),bd=10,height=1,width=2,command =lambda :btnclick(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text="2",font=("airel",19,"bold"),bd=10,height=1,width=2,command =lambda :btnclick(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text="3",font=("airel",19,"bold"),bd=10,height=1,width=2,command=lambda :btnclick(3))
btn3.grid(row=3,column=2)
btnsub=Button(root,text="-",font=("airel",19,"bold"),bd=10,height=1,width=2,command=lambda :btnclick("-"))
btnsub.grid(row=3,column=3)

btnclear=Button(root,text="AC",font=("airel",19,"bold"),bd=10,height=1,width=2,command=btnclear)
btnclear.grid(row=4,column=0)
btn0=Button(root,text="0",font=("airel",19,"bold"),bd=10,height=1,width=2,command=lambda :btnclick(0))
btn0.grid(row=4,column=1)
btndiv=Button(root,text="/",font=("airel",19,"bold"),bd=10,height=1,width=2,command=lambda :btnclick("/"))
btndiv.grid(row=4,column=2)
btnequal=Button(root,text="=",font=("airel",19,"bold"),bd=10,height=1,width=2,command=btneqaul)
btnequal.grid(row=4,column=3)

root.mainloop()
# santosh