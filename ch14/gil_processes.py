from multiprocessing import Process

def task():
    str(2**1000000)

if __name__ == '__main__':
    p1, p2 = Process(target=task), Process(target=task)
    p1.start()
    p2.start()
