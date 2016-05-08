import sys
import unittest
import subprocess
from pathlib import Path
from argparse import ArgumentParser

ROOTDIR = Path(__file__).parent
LOGBOOK_A = str(ROOTDIR.joinpath('pitti.log'))
LOGBOOK_B = str(ROOTDIR.joinpath('uffizi.log'))

parser = ArgumentParser()
parser.add_argument('-f', '--file', default='visitors.py')
parser.add_argument('unittest_args', nargs='*')
args = parser.parse_args()
SCRIPT = str(ROOTDIR.joinpath(args.file))


class TestVisitors(unittest.TestCase):

    def setUp(self):
        self.cmd = ['python', SCRIPT, '-a', LOGBOOK_A, '-b', LOGBOOK_B]

    def test_only_palazzo_pitti(self):
        out = subprocess.check_output(self.cmd)
        self.assertEqual(
            out,
            b'Hanno visitato il museo A ma non il B:\n'
            b'Armin Ronacher\n'
            b'Guido van Rossum\n'
            b'Linus Torvalds\n'
            b'Ned Batchelder\n'
            b'Nick Coghlan\n')


if __name__ == '__main__':
    sys.argv[1:] = args.unittest_args
    unittest.main()
