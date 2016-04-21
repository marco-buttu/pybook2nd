import argparse
from operator import itemgetter
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument(
    '-f', '--file',
    type=argparse.FileType(),
    required=True,
    help='File da processare')
args = parser.parse_args()

result = []
for line in args.file:
    try:
        ta_str, tb_str = line.split(',')
        ta = datetime.strptime(ta_str.strip(), '%d/%m/%Y')
        tb = datetime.strptime(tb_str.strip(), '%d/%m/%Y h%H:%M:%S')
        diff = abs(ta - tb)
        fmt = '%Y/%b/%d'  # String format
        result.append((ta.strftime(fmt), tb.strftime(fmt), diff.days))
    except ValueError:
        pass

for item in sorted(result, key=itemgetter(-1), reverse=True):
    print(*item, sep=' - ')
