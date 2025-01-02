import os
from os.path import isdir,join
from threading import Thread,Lock
import time
from wait_group import WaitGroup


mutex = Lock()
matches = []

def file_seach(root,filename,wait_group):
    
    print(f"Searching in {root} for {filename}")
    for file in os.listdir(root):
        full_path = join(root,file)
        if filename == file:
                mutex.acquire()
                matches.append(full_path)
                mutex.release()
        elif isdir(full_path):
                wait_group.add(1)
                t= Thread(target=file_seach, args=(full_path,filename,wait_group))  
                t.start()
    wait_group.done()    


def main():
    wait_group = WaitGroup()
    wait_group.add(1)    
    t= Thread(target=file_seach, args=("C:\Games","content.rpf",wait_group))  
    t.start()
    wait_group.wait()
    for m in matches:
          print("Found",m)

if __name__ == "__main__":
    main()