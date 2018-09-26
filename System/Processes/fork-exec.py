"starts programs until you type 'q'"

import os

parm = 0
while True:
    parm += 1
    pid = os.fork()
    if pid == 0:                                                # if we're in a CHILD process
        os.execlp('python', 'python', 'child.py', str(parm))    # overlay program
        assert False, 'error starting program'                  # should'nt return
    else:
        print('Child is', pid)                                  # else if we're in the PARENT process
        if input() == 'q': break
