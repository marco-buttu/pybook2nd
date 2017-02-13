from multiprocessing import Process, Queue
import requests

queue = Queue()

def pep_length(pep_code: int):
    BASE_URL = 'https://www.python.org/dev/peps'
    r = requests.get(f'{BASE_URL}/pep-{pep_code:#04d}/')
    queue.put(len(r.content))

if __name__ == '__main__':
    counter = 0
    pep_codes = (7, 20)
    for pep_code in pep_codes:
        p = Process(target=pep_length, args=(pep_code,))
        p.start()
    for _ in range(2):
        counter += queue.get(timeout=10)
    print(f'PEP {pep_codes} lunghe {counter} bytes')
