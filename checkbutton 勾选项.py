import tkinter as tk
window=tk.Tk()
window.title('checkbutton 多项选择')
window.geometry('150x150')

l=tk.Label(window,bg='yellow',width=20,text=' ')
l.grid(row=0,column=0)
var1=tk.IntVar() #int变量
var2=tk.IntVar()
def print_selection():
    if (var1.get()+var2.get())==0:
        l.config(text='l do not love either')
    elif(var1.get()+var2.get())==2:
        l.config(text='l love both')
    elif(var1.get()==0)and(var2.get()==1):
        l.config(text='l love cpp')
    else:
        l.config(text='l love python')
#checkbutton勾选项onvalue表示勾选时将其赋值给var1，command调用函数
c1=tk.Checkbutton(window,text='python',variable=var1,onvalue=1,offvalue=0,command=print_selection)
c1.grid(row=1,column=0)
c2=tk.Checkbutton(window,text='Cpp',variable=var2,onvalue=1,offvalue=0,command=print_selection)
c2.grid(row=2,column=0)
window.mainloop()
