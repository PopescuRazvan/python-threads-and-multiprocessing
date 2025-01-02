

from threading import Thread,Condition
import time

class StingySpendy:
    money = 100
    cv = Condition()
    def stingy(self):
        for i in range(10000):
            self.cv.acquire()
            self.money += 10
            self.cv.notify()
            self.cv.release()
        print("Stingy: ")

    def spendy(self):
        for i in range(1000): 
            self.cv.acquire()
            while self.money < 20:
                self.cv.wait()
            self.money -= 20
            if self.money < 0:
                print("Out of money")
            self.cv.release()
        print("Spendy: ")

ss=StingySpendy()
Thread(target=ss.stingy, args=()).start()
Thread(target=ss.spendy, args=()).start()
time.sleep(3)

print(ss.money)