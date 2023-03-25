from tkinter import *
from Grip import *

def main():
    root = Tk()
    root.geometry("200x200")
    root.resizable(0, 0)
    root.overrideredirect(1)

    back = Frame(root, bg="grey")
    back.pack_propagate(0)
    back.pack(fill=BOTH, expand=1)

    grip = Grip(back, goingBeyond=False)

    root.mainloop()

main()