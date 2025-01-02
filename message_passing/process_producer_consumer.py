import time
from multiprocessing import Process, Queue

def consumer(q):
    while True:
        txt=    q.get()
        print(txt)
        time.sleep(1)

def producer(q):    
    while True:
        q.put("hello")
        print("message sent")

if __name__ == "__main__":
    q = Queue(maxsize=10)
    p1 = Process(target=consumer, args=(q,))
    p2 = Process(target=producer, args=(q,))


    p1.start()
    p2.start()