import requests

def pep_length(pep_code: int):
    BASE_URL = 'https://www.python.org/dev/peps'
    r = requests.get(f'{BASE_URL}/pep-{pep_code:#04d}/')
    return len(r.content)

if __name__ == '__main__':
    counter = 0
    pep_codes = (7, 20)
    for pep_code in pep_codes:
        counter += pep_length(pep_code)
    print(f'PEP {pep_codes} lunghe {counter} bytes')
