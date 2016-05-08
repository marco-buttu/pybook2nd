import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-a', '--logbook_a',
    type=argparse.FileType(),
    required=True,
    help='Logbook del museo A')
parser.add_argument(
    '-b', '--logbook_b',
    type=argparse.FileType(),
    required=True,
    help='Logbook del museo B')
args = parser.parse_args()

visitors_a = set(args.logbook_a)
visitors_b = set(args.logbook_b)
print('Hanno visitato il museo A ma non il B:')
for visitor in sorted(visitors_a - visitors_b):
    print(visitor, end='')
