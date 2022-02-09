import tkinter
import tkinter as tk
entry_root=tk.Tk()
entry_root.title('输入文本')
entry_root.geometry('200x200')
e=tk.Entry(entry_root,show=None) #输入文本框
e.pack()
def insert_ponit():
    var=e.get() #获取entry的文字内容
    t.insert('insert',var) #将entry文本内容插入到text中 'insert'代表按自己的期望（鼠标光标）插入
def insert_end():
    var=e.get()
    t.insert('end',var) #insert(1.1,var) # 'end'代表插入text最后
def clear_text():
    t.delete(1.0,tkinter.END) #与insert一样的索引模式start:第一行.第一列，end（用tkinter.END代表
b1=tk.Button(entry_root,text='insert point',width=15,height=2,command=insert_ponit)
b1.pack()

b2=tk.Button(entry_root,text='insert end',command=insert_end)
b2.pack()

b3=tk.Button(entry_root,text='clear',bg='red',command=clear_text)
b3.pack()

t=tk.Text(entry_root,height=2)
t.pack()
entry_root.mainloop()
