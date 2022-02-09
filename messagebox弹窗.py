import tkinter as tk
from tkinter import messagebox

window=tk.Tk()
window.title('my window')
window.geometry('200x200')


def hit_me():#不同的弹窗类型
    # messagebox.showinfo(title='Hi',message='okok')
    # messagebox.showwarning(title='Hi',message='NONONO')
    # messagebox.showerror(title='Hi',message='Error')
    # messagebox.askquestion(title='Hi',message='yes no')
    messagebox.askokcancel(title='Hi', message='ok cancel') #return True Flase
    # print(messagebox.askokcancel(title='Hi',message='ok cancel'))

tk.Button(window,text='hit me',command=hit_me).pack()

#TODO pack grid place 部件放置位置

# tk.Label(window,text='1').pack(side='top')# top left bottom right

# for i in range(4):
#     for j in range(3):
#         tk.Label(window,text='1').grid(row=i,column=j) padx pady x,y 方向上的扩展
#

# tk.Label(window,text='1').place(x=10,y=100,anchor='nw')






window.mainloop()