from threading import Thread

result = 0

def task():
    global result
    for i in range(10**6):
        result += 1

if __name__ == '__main__':
    t1, t2 = Thread(target=task), Thread(target=task)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('result:', result)
