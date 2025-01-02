import multiprocessing
from multiprocessing.context import Process

import time

def print_array_contents(array):    
    while True:
        print(*array,sep=",")
        time.sleep(1)



if __name__ == "__main__":
    array = multiprocessing.Array('i', [-1]*10,lock=True)
    p = Process(target=print_array_contents, args=([array]))
    p.start()
    for i in range(10):
        time.sleep(2)
        for j in range(10):
            array[j] = i