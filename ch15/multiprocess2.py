from multiprocessing import Process

mylist = [1, 2, 3]

def foo():
    mylist.append(4)
    print('Valore di mylist nel figlio:', mylist)


if __name__ == '__main__':
    p = Process(target=foo)
    p.start()
    p.join()  # Attendo che il figlio termini
    print('Valore di mylist nel padre:', mylist)
