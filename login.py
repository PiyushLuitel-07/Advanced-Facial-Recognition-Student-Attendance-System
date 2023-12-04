from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Login")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.wm_state('zoomed')
root.configure(bg="#fff")

img=PhotoImage(file='login.png')
# Resize the image to the desired width and height
Label(root,image=img,bg='white').place(x=200,y=200)

frame=Frame(root,width=600,height=500,bg="#F5F5F5")
frame.place(x=620,y=130)
#57a1f8
heading=Label(frame,text='Sign in',fg='#57a1f8',bg='#F5F5F5',font=('Microsoft YaHei UI Light',40))
heading.place(x=230-15,y=5+15)

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user=Entry(frame,width=25,fg='#002D62',border=0,bg="#F5F5F5",font=('Microsoft YaHei UI Light',15))
user.place(x=230+15,y=95+90)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=200-50,y=128+90)

def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code=Entry(frame,width=25,show='*',fg='#002D62',border=0,bg="#F5F5F5",font=('Microsoft YaHei UI Light',15))
code.place(x=230+15,y=165+90)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=200-50,y=198+90)

Button(frame,width=25,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,font=('Microsoft YaHei UI Light',15)).place(x=170-15,y=198+90+60)


root.mainloop()