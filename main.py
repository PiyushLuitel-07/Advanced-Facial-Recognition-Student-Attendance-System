from tkinter import*
from tkinter import ttk
# from PIL import Image,ImageTk

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        # Set the window size and position in the center of the screen
        root.geometry(f"{screen_width}x{screen_height}+0+0")
        # Maximize the window
        root.wm_state('zoomed')
        self.root.title("Face Recognition System")



if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
