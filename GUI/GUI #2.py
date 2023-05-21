# Creating Lable , geometry , maxsize and minsize in Tkinter GUI.
from tkinter import *


gui_root  = Tk()

# Width x Height
gui_root.geometry("555x444")

# set maxsize Width , Height
gui_root.maxsize(888,666)

# set minsize Width , Height
gui_root.minsize(222,111)

# Creating lable 
hello = Label(text="Tkinter")
hello.pack()

gui_root.mainloop()