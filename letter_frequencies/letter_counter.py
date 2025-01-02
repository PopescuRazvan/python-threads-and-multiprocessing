import json
import urllib.request
import time
from threading import Thread,Lock

finished_count=0

def count_letters(url,frequncy,mutex):
    response = urllib.request.urlopen(url)
    text = str(response.read())
    mutex.acquire()
    for l in text:
        letter = l.lower()
        if letter in frequncy:
            frequncy[letter] += 1
    global finished_count
    finished_count += 1
    mutex.release()


def main():
    frequncy = {}
    mutex = Lock()
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequncy[c] = 0
    start = time.time()
    
    for i in range(1000,1020):
        Thread(target=count_letters, args=(f"https://rfc-editor.org/rfc/rfc{i}.txt",frequncy,mutex)).start()
    while True:
        mutex.acquire()
        if finished_count == 20:
            break
        mutex.release()
    end = time.time()

    print(json.dumps(frequncy))
    print (f"Time: {end-start}")

if __name__ == "__main__":
    main()