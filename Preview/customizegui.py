

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter102 import MyGui

class CustomGUI(MyGui):
    def reply(self):
        """
        Set the title and message of the window
        """
        showinfo(title='popup', message='Ouch!')

if __name__ == '__main__':
    CustomGUI().pack()
    mainloop()
