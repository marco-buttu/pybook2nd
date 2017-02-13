from multiprocessing import Process, Queue

queue = Queue()

def foo():
    mylist = queue.get()
    mylist.append(4)
    print('Nel figlio:', mylist)
    queue.put('ciao')


if __name__ == '__main__':
    mylist = [1, 2, 3]
    queue.put(mylist)
    p = Process(target=foo)
    p.start()
    p.join()
    value = queue.get()
    print('Nel padre:', mylist, value)
