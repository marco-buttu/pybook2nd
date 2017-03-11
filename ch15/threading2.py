from threading import Thread

mylist = [1, 2, 3]

def foo():
    mylist.append(4)
    print('Valore di mylist nel thread:', mylist)


if __name__ == '__main__':
    t = Thread(target=foo)
    t.start()
    t.join()  # Attendo che il thread termini
    print('Valore di mylist nel processo:', mylist)
