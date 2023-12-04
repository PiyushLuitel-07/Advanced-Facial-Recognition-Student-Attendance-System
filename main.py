# # Tkinter library to create a graphical user interface (GUI)
# from tkinter import*
# # ttk: Themed Tkinter, a module within Tkinter that provides access to the Tk themed widget set.
from tkinter import ttk
# # library for opening, manipulating, and saving many different image file formats.
# # from PIL import Image,ImageTk

# class Face_Recognition_System:
#     def __init__(self,root):
#         # self.root is an instance variable that holds the reference to the main window
#         self.root=root
#         screen_width = root.winfo_screenwidth()
#         screen_height = root.winfo_screenheight()
#         # Set the window size and position in the center of the screen
#         root.geometry(f"{screen_width}x{screen_height}+0+0")
#         # Maximize the window
#         root.wm_state('zoomed')
#         self.root.title("Face Recognition System")



# if __name__=="__main__":
#     # An instance of the Tk class (which represents the main window) is created and assigned to the variable root.
#     root=Tk()
#     obj=Face_Recognition_System(root)
#     # The mainloop() method starts the Tkinter event loop, and the GUI window is displayed.
#     root.mainloop()

from tkinter import *

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")

        # Set the window size and position in the center of the screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}+0+0")
        root.wm_state('zoomed')

        root.configure(bg='#2C3539')
        #002147

        # Create login frame
        login_frame = Frame(root, bg='#2C3539', padx=20, pady=20)
        login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Username Label and Entry
        username_label = Label(login_frame, text="Username", font=('Lato', 14), bg='white')
        username_label.grid(row=0, column=0)
        self.username_entry = Entry(login_frame, font=('Lato-Light', 14))
        self.username_entry.grid(row=1, column=0, pady=10)

        # Password Label and Entry
        password_label = Label(login_frame, text="Password", font=('Lato-Light', 14), bg='white')
        password_label.grid(row=2, column=0)
        self.password_entry = Entry(login_frame, show='*', font=('Lato-Light', 14))
        self.password_entry.grid(row=3, column=0, pady=10)

        # Login Button
        login_button = Button(login_frame, text="Login", command=self.login, font=('Lato-Light', 14))
        login_button.grid(row=4, columnspan=2, pady=10)

        # Welcome Label (to be displayed after login)
        self.welcome_label = Label(root, text="", font=('Lato-Light', 16, 'bold'), bg='black', fg='white')
        self.welcome_label.pack(pady=20)

    def login(self):
        # Get the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # For demonstration purposes, check if the username and password are not empty
        if username and password:
            welcome_message = f"Welcome, {username}!"
            self.welcome_label.config(text=welcome_message)
        else:
            self.welcome_label.config(text="Invalid username or password")

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

