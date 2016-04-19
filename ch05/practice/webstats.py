#!/usr/bin/env python
import argparse
import collections
from datetime import datetime, date, timedelta

def str2date(string):
    """Data una stringa, restituisci un datetime.date.

    La stringa deve essere nella forma 'year month day'.
    Un esempio di utilizzo:

        >>> str2date('2017 1 16')
        datetime.date(2017, 1, 16)
    """
    return date(*[int(item) for item in string.split()])

parser = argparse.ArgumentParser()
parser.add_argument(
    '-f', '--file',
    type=argparse.FileType(),
    required=True,
    help='File da processare')
parser.add_argument(
    '-d', '--date',
    type=str2date,
    required=True,
    help="Data: 'y m d'")
parser.add_argument(
    '-r', '--radius',
    default=0,
    type=int,
    choices=range(3))
args = parser.parse_args()

hits = []
# strfmt: [day/month/year:hour:minute:second time-zone]
strfmt = '[%d/%b/%Y:%H:%M:%S %z]'  # http://strftime.org/
for line in args.file:
    try:
        ip_address, hit_time = line.split(' - ')
    except ValueError:
        continue
    hit_date = datetime.strptime(hit_time.strip(), strfmt)
    diff = args.date - hit_date.date()
    if abs(diff) <= timedelta(days=args.radius):
        hits.append(ip_address)

unique_visitors = set(hits)
counter = collections.Counter()
for ip_address in hits:
    counter[ip_address] += 1
print('Numero di hit:', len(hits))
if hits:
    print('Visitatori unici:', len(unique_visitors))
    print('Maggior numero di hit:')
    for ip_address, ip_hits in counter.most_common(3):
        print(ip_address, ip_hits, sep=' -> ')
