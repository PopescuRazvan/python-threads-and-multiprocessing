from multiprocessing import Process, Pipe
import time


def ping(pipe_conn):
    while True:
        pipe_conn.send(["ping",time.time()])
        pong = pipe_conn.recv()
        print(pong)
        time.sleep(1)


def pong(pipe_conn):    
    while True:
        ping = pipe_conn.recv()
        print(ping)
        time.sleep(1)
        pipe_conn.send(["pong",time.time()])


if __name__ == "__main__":
    parent_conn,child_conn = Pipe()
    p1 = Process(target=ping, args=(child_conn,))
    p2 = Process(target=pong, args=(parent_conn,))
    p1.start()
    p2.start()
