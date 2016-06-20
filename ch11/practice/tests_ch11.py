import sys
import unittest
import subprocess
from pathlib import Path
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-f', '--file', default='hotspots.py')
parser.add_argument('unittest_args', nargs='*')
args = parser.parse_args()

ROOTDIR = Path(__file__).parent
SCRIPT = str(ROOTDIR.joinpath(args.file))
BASECMD = ['python', SCRIPT, '--file']


class TestRanges(unittest.TestCase):

    def test_only_ranges(self):
        """Only ranges (no points): test1.png, test1.dat."""
        expected = (
            b'08:47:42.354-09:16:27.155;3\n'
            b'09:58:04.024-10:06:27.155;3\n'
            b'11:59:34.635-12:30:02.340;3\n'
        )
        self.check('test1.dat', expected)
        
    def test_only_points(self):
        """Only points (no ranges): test2.png, test2.dat."""
        expected = (
            b'10:06:27.155-10:06:27.155;5\n'
            b'12:30:02.340-12:30:02.340;5\n'
        )
        self.check('test2.dat', expected)
 
    def test_points_and_ranges(self):
        """Points and ranges: test3.png, test3.dat."""
        expected = (
            b'08:47:42.354-09:16:27.155;5\n'
            b'10:06:27.155-10:06:27.155;5\n'
            b'11:59:34.635-12:13:01.977;5\n'
            b'12:30:02.340-12:30:02.340;5\n'
        )
        self.check('test3.dat', expected)
 
    def test_points_increment(self):
        """Increment of the `points` dictionary values.
   
        Figure test4.png reports a case in which there are some
        starting times and ending times with the same value, but
        in the `time` list the starting times come after the ending
        times, and viceversa. In that case, we have to increment the
        point value depending of the previous time type:
        
        * current is starting, previous is ending, increment of 1
        * current is ending, previous is ending, increment of 2
        """
        expected = (
            b'09:16:27.155-09:16:27.155;4\n'
            b'11:16:27.155-11:16:27.155;4\n'
        )
        self.check('test4.dat', expected)

    def check(self, logfile, expected):
        LOGFILE = str(ROOTDIR.joinpath(logfile))
        cmd = BASECMD + [LOGFILE]
        out = subprocess.check_output(cmd)
        self.assertEqual(out, expected)


if __name__ == '__main__':
    sys.argv[1:] = args.unittest_args
    unittest.main()
