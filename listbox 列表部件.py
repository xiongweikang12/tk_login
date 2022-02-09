#TODO listbox
import tkinter as tk
root=tk.Tk()
root.title('listbox')
root.geometry('200x200')
var1=tk.StringVar()#字符串变量
l=tk.Label(root,bg='yellow',width=4,textvariable=var1) #标签的可变textvariable=var1
l.pack()

def print_selection():
    var1.set(lb.get(lb.curselection())) #b1 print selection按钮启动command设置var1，textvariable随之变化
    #设置内容为listbox.get得到的curselection（选项）

b1=tk.Button(root,text="print selection",width=15,height=2,command=print_selection)
b1.pack()
var2=tk.StringVar()
var2.set((11,22,33,44)) #设置var2,给listvariable赋值
lb=tk.Listbox(root,listvariable=var2) #listbox的listvarable
list_item=['熊伟康','weikang','wei']
for item in list_item:#遍历列表内容insert进入listbox中
    lb.insert('end',item) #insert最后
# lb.insert(1,'frist') #insert插入索引的位置
# lb.insert(2,'second')
lb.pack()
root.mainloop()
