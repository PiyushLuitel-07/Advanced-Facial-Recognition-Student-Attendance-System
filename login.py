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

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='#F5F5F5',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=230,y=5)


root.mainloop()