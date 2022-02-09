import tkinter
import tkinter as tk
from tkinter import messagebox
import pickle

window=tk.Tk()
window.title('welcom to kk python')
window.geometry('400x400')
canvas=tk.Canvas(window,height=150,width=400)
image_file=tk.PhotoImage(file='welcom.gif')
image=canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')

tk.Label(window,text='username:').place(x=50,y=150)
tk.Label(window,text='password:').place(x=50,y=190)
var_name=tk.StringVar()
var_name.set('1761322862@qq.com')
entry_user_name=tk.Entry(window,textvariable=var_name)
entry_user_name.place(x=160,y=150)
var_password=tk.StringVar()
var_password.set('13803537357')
entry_user_password=tk.Entry(window,textvariable=var_password,show='*')
entry_user_password.place(x=160,y=190)
container_info=[]

#login and sign up
def sign_up_yes():

    def SignUp_to_kk():
        to_kk_name=new_name.get()
        to_kk_password=new_password.get()
        to_kk_confirm_password=new_comfirm_password.get()
        with open('user_info.pickle','rb') as user_file_top:
            user_info_top=pickle.load(user_file_top)
            if {to_kk_name:to_kk_password} not in container_info :
                if to_kk_password==to_kk_confirm_password:
                    with open('user_info.pickle','wb') as user_file_top:
                        user_info_top={to_kk_name:to_kk_password}
                        pickle.dump(user_info_top,user_file_top)
                        container_info.append(user_info_top)
                    messagebox.showinfo(title='注册成功',message='注册成功，welcom')
                    window_sign_up.destroy()
                else:
                    messagebox.showwarning(title='警告',message='确定密码与密码不符')
                    entry_new_ComfirmPassword.delete(0,tkinter.END)
                    entry_new_password.delete(0,tkinter.END)
            else:
                messagebox.showwarning(title='警告',message='账号已经存在,请重新设置账号')
                entry_new_name.delete(0,tkinter.END)
                entry_new_password.delete(0,tkinter.END)
                entry_new_ComfirmPassword.delete(0,tkinter.END)



    window_sign_up=tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign Up window')
    new_name=tk.StringVar()
    tk.Label(window_sign_up,text='User Name').place(x=10,y=10)
    entry_new_name=tk.Entry(window_sign_up,textvariable=new_name)
    entry_new_name.place(x=150,y=10)

    new_password=tk.StringVar()
    tk.Label(window_sign_up,text='Password').place(x=10,y=50)
    entry_new_password=tk.Entry(window_sign_up,textvariable=new_password)
    entry_new_password.place(x=150,y=50)

    new_comfirm_password = tk.StringVar()
    tk.Label(window_sign_up, text='Comfirm Password').place(x=10, y=90)
    entry_new_ComfirmPassword = tk.Entry(window_sign_up, textvariable=new_comfirm_password)
    entry_new_ComfirmPassword.place(x=150, y=90)

    button_confirm_SignUp=tk.Button(window_sign_up,text='comfrim',command=SignUp_to_kk)
    button_confirm_SignUp.place(x=150,y=130)




def login_yes():
    user_name=var_name.get()
    user_password=var_password.get()
    try :
        with open('user_info.pickle','rb') as user_file:
            user_info=pickle.load(user_file)
    except FileNotFoundError:
        with open('user_info.pickle','wb') as user_file:
            user_info={'admin':'admin'}
            pickle.dump(user_info,user_file)
            container_info.append(user_info)

    if {user_name:user_password} in container_info:
        # if user_password==user_info[user_name]:
        messagebox.showinfo(title='登录成功',message='welcom  how are you !')
        # print(messagebox.askretrycancel(title='登录失败',message='请重试或者再注册')) retry-->true cancel-->false
        # else:
        #     messagebox.showerror(title='密码错误',message='密码错误，重新输入')
        #     entry_user_password.delete(0,tkinter.END)
    else:
        if messagebox.askretrycancel(title='账号不存在',message='账号注册'):
            entry_user_password.delete(0,tkinter.END)
            entry_user_name.delete(0,tkinter.END)
        else:
            if messagebox.askokcancel(title='即将注册', message='You have not sign up yet .Sign Up today'):
                sign_up_yes()
            else:
                exit()




button_login=tk.Button(window,text='login',command=login_yes)
button_login.place(x=160,y=230)
button_SignUp=tk.Button(window,text='sign up',command=sign_up_yes)
button_SignUp.place(x=260,y=230)



if __name__=='__main__':
    window.mainloop()