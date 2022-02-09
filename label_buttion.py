
#TODO 静态标签与按钮控件

import tkinter as tk

root=tk.Tk() #窗口对象（类)
root.title("my window") #题目
root.geometry('200x100') #大小
var=tk.StringVar() #tk的字符变量
l=tk.Label(root,textvariable=var,bg='green',font=('Arial',12),width=15,height=2)
#标签，（对象，文本，可变文本，background背景颜色 字体宽高）
l.pack() #每创建一个都要lay pack放置
on_hit=False #全局变量
def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set('you hit me') #改变var,相当于赋值给textvariable'you hit me'
    else:
        on_hit=False#保证按钮再次时候，重新设置var（清空），设置on_hit为False为下次促发
        var.set('')
b=tk.Button(root,text='hit me',width=15,height=2,command=hit_me)
#按钮（对象，文本，宽高，按钮促发的command（相当于函数的调用）hit_me()）
b.pack() #lay 安置
root.mainloop() #启动


