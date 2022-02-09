import tkinter as tk
# from PIL import Image, ImageTk

window=tk.Tk()
window.title("my window canvas")
window.geometry('200x200')
canvas=tk.Canvas(window,bg='blue',height=100,width=200)#画布
# img = Image.open('boyi.jpg')
image_file=tk.PhotoImage(file='yuyuyu.gif')
image=canvas.create_image(0,0,anchor='nw',image=image_file)


canvas.pack()
# b=tk.Button(window,text='move',command=moveit).pack()

window.mainloop()