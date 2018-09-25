

from tkinter import *
from tkinter.messagebox import showinfo

class MyGui(Frame):
    """
    Subclass of the tkinter Frame widget which is a container for other widgets.
    Creates a button with text 'press' that calls the 'reply' method
    """
    def __init__(self, parent=None):
        """
        Initialize the button
        """
        Frame.__init__(self, parent)
        button = Button(self, text = 'press', command = self.reply)
        button.pack()

    def reply(self):
        """
        Set the title and message of the window
        """
        showinfo(title='popup', message='Button pressed!')

if __name__ == '__main__':
    window = MyGui() # main window
    window.pack()
    window.mainloop()
