import time
from threading import Thread
def do_work():
    print("Thread is running")
    time.sleep(1)
    i=0 
    for i in range(2000000):
        i += 1
    print("Thread is done")


if __name__ == "__main__":
    for i in range(5):
        t= Thread(target=do_work, args=())
        t.start()
        #do_work()