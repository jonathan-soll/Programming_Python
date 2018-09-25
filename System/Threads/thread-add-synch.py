"prints 200 each time, because shared resource access synchronized"

import threading, time
count = 0

def adder(addlock):
    global count                                                # access the global 'count' variable
    with addlock:                                               # auto acquire/release around stmt
        count = count + 1
    time.sleep(0.5)
    with addlock:
        count = count + 1                                       # only 1 thread updating at once

addlock = threading.Lock()
threads = []
for i in range(100):
    thread = threading.Thread(target=adder, args=(addlock,))    # spawn a thread
    thread.start()                                              # run the adder function
    threads.append(thread)

for thread in threads: thread.join()
print(count)
