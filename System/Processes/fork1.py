"forks chils processes until you type 'q', doesn't work on PC because forking is not supported"

import os

def child():
    print('Hello from child', os.getpid())
    os._exit(0)     # else goes back to parent loop

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)
        if input() == 'q': break

parent()
