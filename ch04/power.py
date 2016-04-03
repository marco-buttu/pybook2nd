"""Data una base e un esponente, stampa la potenza.

Utilizzo: python power.py -b BASE -e ESPONENTE.
Esempio: `python power.py -b 5 -e 3` restituisce 125."""
import sys
try:
    for index, item in enumerate(sys.argv):
        if item == '-b':
            base = sys.argv[index+1]
        elif item == '-e':
            exp = sys.argv[index+1]
    print(int(base) ** int(exp))
except (IndexError, ValueError, NameError):
    print(__doc__)
