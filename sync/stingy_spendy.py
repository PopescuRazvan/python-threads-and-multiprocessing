from threading import Thread,Lock
import time

class StingySpendy:
    money = 100
    mutex = Lock()
    def stingy(self):
        for i in range(10000000):
            self.mutex.acquire()
            self.money += 10
            self.mutex.release()
        print("Stingy: ")

    def spendy(self):
        for i in range(10000000): 
            self.mutex.acquire()
            self.money -= 10
            self.mutex.release()
        print("Spendy: ")

ss=StingySpendy()
Thread(target=ss.stingy, args=()).start()
Thread(target=ss.spendy, args=()).start()
time.sleep(15)

print(ss.money)