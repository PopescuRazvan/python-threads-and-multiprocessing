import time
from threading import Thread

def child():
    print("Child is running")
    time.sleep(5)
    print("Child is done")

t1 = Thread(target=child)
t1.start()
print("Main is waiting")
t1.join()
print("Main is running")