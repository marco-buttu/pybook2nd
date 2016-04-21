import sys
import unittest
import subprocess
from pathlib import Path
from argparse import ArgumentParser
from sort import sortdict

ROOTDIR = Path(__file__).parent
LOGFILE = str(ROOTDIR.joinpath('timestats.log'))

parser = ArgumentParser()
parser.add_argument('-f', '--file', default='timestats.py')
parser.add_argument('unittest_args', nargs='*')
args = parser.parse_args()
SCRIPT = str(ROOTDIR.joinpath(args.file))


class TestSortdict(unittest.TestCase):

    def test(self):
        d = {'a': 11, 'b': 8, 'c': 33, 'd': 0, 'e': 5}
        expected = [('d', 0), ('e', 5), ('b', 8), ('a', 11), ('c', 33)]
        result = sortdict(d)
        self.assertListEqual(result, expected)

class TestTimestats(unittest.TestCase):

    def setUp(self):
        self.cmd = ['python', SCRIPT, '-f', LOGFILE]

    def test(self):
        out = subprocess.check_output(self.cmd)
        self.assertEqual(
            out,
            b'2017/Oct/18 - 2018/Oct/18 - 365\n'
            b'2016/Jun/15 - 2016/May/15 - 30\n'
            b'2018/Dec/17 - 2018/Dec/22 - 5\n'
            b'2018/Dec/29 - 2018/Dec/31 - 2\n'
            b'2017/Mar/01 - 2017/Mar/02 - 1\n'
            b'2017/May/06 - 2017/May/06 - 0\n')


if __name__ == '__main__':
    sys.argv[1:] = args.unittest_args
    unittest.main()
