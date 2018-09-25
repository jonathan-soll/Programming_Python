from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    """
    Set the title and message of the window
    """
    showinfo(title='popup', message='Button pressed!')

window = Tk() # main window
button = Button(window, text = 'press', command = reply) # create a button in the 'window' container that does the 'reply' function
button.pack()
window.mainloop()
