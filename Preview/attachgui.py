"""

"""

from tkinter import *
from tkinter102 import MyGui

# main app window
mainwin = Tk()
Label(mainwin, text = __name__).pack()

# popup window
popup = Toplevel() # create another widget
Label(popup, text = 'Attach').pack(side=LEFT) # add a label to left side of the widget
MyGui(popup).pack(side=RIGHT)  # attach my frame
mainwin.mainloop()
