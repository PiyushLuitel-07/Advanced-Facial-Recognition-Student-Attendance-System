# Tkinter library to create a graphical user interface (GUI)
from tkinter import*
# ttk: Themed Tkinter, a module within Tkinter that provides access to the Tk themed widget set.
from tkinter import ttk
# library for opening, manipulating, and saving many different image file formats.
# from PIL import Image,ImageTk

class Face_Recognition_System:
    def __init__(self,root):
        # self.root is an instance variable that holds the reference to the main window
        self.root=root
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        # Set the window size and position in the center of the screen
        root.geometry(f"{screen_width}x{screen_height}+0+0")
        # Maximize the window
        root.wm_state('zoomed')
        self.root.title("Face Recognition System")



if __name__=="__main__":
    # An instance of the Tk class (which represents the main window) is created and assigned to the variable root.
    root=Tk()
    obj=Face_Recognition_System(root)
    # The mainloop() method starts the Tkinter event loop, and the GUI window is displayed.
    root.mainloop()
