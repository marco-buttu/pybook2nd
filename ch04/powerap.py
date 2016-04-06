"""Data una base e un esponente, stampa la potenza."""
import argparse
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('-b', '--base', type=int, required=True)
parser.add_argument('-e', '--exp', type=int, required=True)
args = parser.parse_args()
print(args.base ** args.exp)
