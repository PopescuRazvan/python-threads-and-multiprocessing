import multiprocessing
def do_work():
    print("Process is running")
    i=0
    for _ in range(200000000):
        i += 1
    print("Process is done")    

if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')
    for i in range(5):
        p= multiprocessing.Process(target=do_work, args=())
        p.start()
        #do_work()