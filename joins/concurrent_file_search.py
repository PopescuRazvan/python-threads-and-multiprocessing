import os
from os.path import isdir,join
from threading import Thread,Lock
import time

mutex = Lock()
matches = []

def file_seach(root,filename):
    print(f"Searching in {root} for {filename}")
    child_threads = []
    for file in os.listdir(root):
        full_path = join(root,file)
        if filename == file:
                mutex.acquire()
                matches.append(full_path)
                mutex.release()
        elif isdir(full_path):
                t= Thread(target=file_seach, args=(full_path,filename))  
                t.start()
                child_threads.append(t)
    for t in child_threads:
        t.join()


def main():
    t= Thread(target=file_seach, args=("c:","content.rpf"))  
    t.start()
    t.join()
    for m in matches:
          print("Found",m)

if __name__ == "__main__":
    main()