from threading import Thread, Lock
import requests

lock = Lock()
counter = 0

def pep_length(pep_code: int):
    BASE_URL = 'https://www.python.org/dev/peps'
    r = requests.get(f'{BASE_URL}/pep-{pep_code:#04d}/')
    global counter
    lock.acquire()
    counter += len(r.content)
    lock.release()

if __name__ == '__main__':
    pep_codes = (7, 20)
    threads = []
    for pep_code in pep_codes:
        t = Thread(target=pep_length, args=(pep_code,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(f'PEP {pep_codes} lunghe {counter} bytes')
