import argparse
parser = argparse.ArgumentParser()
parser.add_argument('file')
args = parser.parse_args()
lines = open(args.file).readlines()
print(lines[0])
