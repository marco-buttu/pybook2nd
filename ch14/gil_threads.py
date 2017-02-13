from threading import Thread

def task():
    str(2**1000000)

if __name__ == '__main__':
    t1, t2 = Thread(target=task), Thread(target=task)
    t1.start()
    t2.start()
