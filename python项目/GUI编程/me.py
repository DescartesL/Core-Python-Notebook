from tkinter import *
def resize(ev=None):
    LableLUO.config(font='Helvetica -%d bold' % ScaleLUO.get())

top = Tk()
top.geometry('200x200')
LableLUO =Label(top,text='Hello,Tk!',font='Helvetica -12 bold' )
LableLUO.pack(fill=Y,expand = 1)


ScaleLUO = Scale(top,from_=10,to=40,orient=HORIZONTAL,command=resize)
ScaleLUO.set(12)
ScaleLUO.pack(fill=X,expand=1)

ButtonLUO = Button(top,text='罗高维大帅比',command=top.quit ,bg='red',fg ='yellow',activeforeground='red',activebackground='white')
ButtonLUO.pack()
mainloop()
