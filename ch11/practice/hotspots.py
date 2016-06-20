#!/usr/bin/env python
import bisect
from argparse import ArgumentParser, FileType
from collections import namedtuple

parser = ArgumentParser()
parser.add_argument('--file', type=FileType(), required=True)
args = parser.parse_args()

times = []
Time = namedtuple('Time', 'value type')
for line in args.file:
    try:
        stime, etime = line.strip().split(',')
        bisect.insort(times, Time(stime, 'starting'))
        bisect.insort(times, Time(etime, 'ending'))
    except ValueError:
        pass

counter, peak, ranges, points = 0, -1, [], {}
prev_time = Time(None, None)
for time in times:
    counter += 1 if time.type == 'starting' else -1
    if time.type == 'starting':
        stime = time
        if counter > peak:
            peak = counter
            ranges = []
    elif counter == peak-1:
        ranges.append((stime.value, time.value))

    if time.value == prev_time.value:
        if time.value in points:
            points[time.value] += 1
        else:
            offset = 1 if time.type == 'starting' else 2
            inc = offset if prev_time.type == 'ending' else 0
            points[time.value] = counter + inc
    prev_time = time

points_peak = max(points.values()) if points else 0
points = [(p, p) for p in points if points[p] == points_peak]
if peak > points_peak:
    hotspots = ranges
elif points_peak > peak:
    peak = points_peak
    hotspots = points
else:
    hotspots = ranges + points

for stime, etime in sorted(hotspots):
    print(f'{stime}-{etime};{peak}')
