"forks chils processes until you type 'q', doesn't work on PC because forking is not supported"

import os

def child():
    print('Hello from child', os.getpid())
    os._exit(0)     # else goes back to parent loop

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:             # if we're in the forked process, run the child() function
            child()
        else:                       # else if we're in the parent process, do this
            print('Hello from parent', os.getpid(), newpid)
        if input() == 'q': break

parent()
