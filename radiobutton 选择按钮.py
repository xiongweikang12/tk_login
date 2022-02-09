import tkinter as tk

window=tk.Tk()
window.title("my window")
window.geometry('150x150')

var1=tk.StringVar()
l=tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()

def print_selection():
    l.config(text='you have seleced'+var1.get())#config修改字体的某一属性值

r1=tk.Radiobutton(window,text='OPtionA',variable=var1,value="A",command=print_selection) #将value赋值给var1（通过variable)
r1.pack()

r2=tk.Radiobutton(window,text='OPtionB',variable=var1,value="B",command=print_selection)
r2.pack()

r3=tk.Radiobutton(window,text='OPtionC',variable=var1,value="C",command=print_selection)
r3.pack()

window.mainloop()
