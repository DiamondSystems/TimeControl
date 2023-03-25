from tkinter import *
from PIL import Image
from pystray import Icon as Tray, Menu as TrayMenu, MenuItem as TrayMenuItem
# from Grip import *


# Global variables
imageIcon = Image.open("./images/icon.ico")


def exitApp(icon, item):
    icon.stop()

def main():
    '''
    root = Tk()
    root.geometry("200x200")
    root.resizable(0, 0)
    root.overrideredirect(1)

    back = Frame(root, bg="grey")
    back.pack_propagate(0)
    back.pack(fill=BOTH, expand=1)

    grip = Grip(back, goingBeyond=False)

    root.mainloop()
    '''


Tray("TimeControl", imageIcon, menu=TrayMenu(
    TrayMenuItem('Quit', exitApp)
    )).run()
main()