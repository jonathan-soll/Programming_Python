import os
import time

for i in range(2):
    print('***************%d***************' % i)
    pid = os.fork()
    if pid == 0:
        print('%d just was created.' % os.getpid())
        time.sleep(3)
    else:
        print('%d just created %d' % (os.getpid(), pid))
        time.sleep(3)
