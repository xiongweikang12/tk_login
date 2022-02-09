import tkinter as tk
window=tk.Tk()
window.title("my window")
window.geometry('200x200')
tk.Label(window,text='on the window').pack()
frm=tk.Frame(window)#母体为window的框架
frm.pack()
frm_1=tk.Frame(frm)#母体为frm的框架
frm_1.pack(side='left')#side框架pack的位置
frm_2=tk.Frame(frm)#母体为frm的框架(在frm的基础上）
frm_2.pack(side='right')
tk.Label(frm_1,text='on the frm_1_1').pack()#根据母体设置标签
tk.Label(frm_1,text='on the frm_1_2').pack()
tk.Label(frm_2,text='on the frm_2').pack()
window.mainloop()