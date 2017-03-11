import urllib.request
import unittest
import subprocess
from pathlib import Path

ROOTDIR = Path(__file__).parent
FILES = ['peps.py', 'peps_threads.py', 'peps_processes.py']


class TestTimestats(unittest.TestCase):

    def setUp(self):
        self.cmds = []
        for file in FILES:
            script = str(ROOTDIR.joinpath(file))
            self.cmds.append(['python', script])

    def test(self):
        BASE_PATH = 'https://www.python.org/dev/peps'
        counter = 0
        for code in (7, 20):
            r = urllib.request.urlopen(
                f'{BASE_PATH}/pep-{code:#04d}')
            counter += len(r.read())
        for cmd in self.cmds:
            out = subprocess.check_output(cmd)
            length = int(out.split()[-2])
            self.assertEqual(length, counter)


if __name__ == '__main__':
    unittest.main()
