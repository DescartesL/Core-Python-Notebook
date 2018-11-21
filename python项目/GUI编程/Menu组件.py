from tkinter import *

root = Tk()
root.geometry('200x200')
def hello():
    w = Label(root,text='hello')
    w.pack(side=TOP)

def about():
    w = Button(root,text='我是大帅比',command=root.quit)
    w.pack(side=BOTTOM)

menubar = Menu(root)

#创建下拉菜单File，然后将其加到顶级的菜单栏中
#用add_command方法创建，最后用add_cascade方法加入到上级菜单中去
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label='Open',command=hello)
filemenu.add_command(label='Save',command = hello)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.quit)
menubar.add_cascade(label='File',menu=filemenu)

#创建另一个下拉菜单Edit
editmenu = Menu(menubar,tearoff=0)
editmenu.add_command(label='Cut',command=hello)
editmenu.add_command(label='Copy',command=hello)
editmenu.add_command(label='Paste',command=hello)
menubar.add_cascade(label='Edit',menu=editmenu)

#创建下拉菜单Help
helpmenu = Menu(menubar,tearoff=0)
helpmenu.add_command(label='About',command=about)
menubar.add_cascade(label='Help',menu=helpmenu)


#显示菜单
root.config(menu=menubar)
mainloop()
