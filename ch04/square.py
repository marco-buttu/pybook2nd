"""Data un numero intero, stampa il suo quadrato.

Utilizzo: python square.py NUMERO_INTERO.
Esempio: `python square.py 6` restituisce 36."""
import sys
try:
    argument = sys.argv[1]
    number = int(argument)
    print(number ** 2)
except(IndexError, ValueError):
    print(__doc__)
