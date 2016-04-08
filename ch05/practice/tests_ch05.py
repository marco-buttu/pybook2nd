import unittest
import subprocess
from pathlib import Path

ROOTDIR = Path(__file__).parent
LOGFILE = str(ROOTDIR.joinpath('test.log'))
SCRIPT = str(ROOTDIR.joinpath('webstats.py'))


class TestMain(unittest.TestCase):

    def setUp(self):
        self.base_cmd = ['python', SCRIPT, '-f', LOGFILE, '-d', '2016 12 31']

    def test_radius0(self):
        out = subprocess.check_output(self.base_cmd)
        self.assertEqual(
            out,
            b'Numero di hit: 2\n'
            b'Visitatori unici: 1\n'
            b'Maggior numero di hit:\n'
            b'87.10.85.230 -> 2\n')

    def test_radius1(self):
        self.base_cmd.extend(['-r', '1'])
        out = subprocess.check_output(self.base_cmd)
        self.assertEqual(
            out,
            b'Numero di hit: 7\n'
            b'Visitatori unici: 3\n'
            b'Maggior numero di hit:\n'
            b'79.56.87.148 -> 4\n'
            b'87.10.85.230 -> 2\n'
            b'54.234.72.18 -> 1\n')

    def test_radius2(self):
        self.base_cmd.extend(['-r', '2'])
        out = subprocess.check_output(self.base_cmd)
        self.assertEqual(
            out,
            b'Numero di hit: 11\n'
            b'Visitatori unici: 5\n'
            b'Maggior numero di hit:\n'
            b'79.56.87.148 -> 4\n'
            b'66.249.73.89 -> 3\n'
            b'87.10.85.230 -> 2\n')

    def test_date_not_found(self):
        """There is no entry with this date."""
        self.base_cmd[-1] = '2020 12 31'
        out = subprocess.check_output(self.base_cmd)
        self.assertEqual(out, b'Numero di hit: 0\n')

    def test_file_not_well_formatted(self):
        self.base_cmd[3] = __file__  # This file
        out = subprocess.check_output(self.base_cmd)
        self.assertEqual(out, b'Numero di hit: 0\n')


if __name__ == '__main__':
    unittest.main()
