import io
import os
import sys
import datetime
import unittest
from unittest.mock import patch, MagicMock
import webstats


FULLPATH = os.path.abspath(__file__)
DIRNAME = os.path.dirname(FULLPATH)
LOGFILE = os.path.join(DIRNAME, 'test.log')


class TestParser(unittest.TestCase):

    def setUp(self):
        self.parser = webstats.getparser()
        self.mock = MagicMock()

    def test_no_arguments(self):
        with patch('argparse.ArgumentParser._print_message', new=self.mock):
            with self.assertRaises(SystemExit):
                self.parser.parse_args([])

    def test_no_filename(self):
        with patch('argparse.ArgumentParser._print_message', new=self.mock):
            with self.assertRaises(SystemExit):
                self.parser.parse_args(['-f'])

    def test_no_date(self):
        with patch('argparse.ArgumentParser._print_message', new=self.mock):
            with self.assertRaises(SystemExit):
                self.parser.parse_args(['-f', LOGFILE, '-d'])

    def test_wrong_date(self):
        with patch('argparse.ArgumentParser._print_message', new=self.mock):
            with self.assertRaises(SystemExit):
                self.parser.parse_args(['-f', LOGFILE, '-d', '2017 2 30'])

    def test_date_conversion(self):
        """Verify the parser converts the date from string to datetime.date."""
        with patch('argparse.ArgumentParser._print_message', new=self.mock):
            args = self.parser.parse_args(
                ['-f', LOGFILE, '-d', '2017 2 20'])
            self.assertEqual(args.date, datetime.date(2017, 2, 20))


class TestGethits(unittest.TestCase):

    def setUp(self):
        self.file = open(LOGFILE)

    def tearDown(self):
        self.file.close()

    def test_date_not_found(self):
        """There is no entry with this date."""
        hits = webstats.gethits(self.file, datetime.date(2020, 12, 31), 0)
        self.assertListEqual(hits, [])

    def test_radius0(self):
        hits = webstats.gethits(self.file, datetime.date(2016, 12, 31), 0)
        expected = ['87.10.85.230', '87.10.85.230']
        self.assertListEqual(hits, expected)

    def test_radius1(self):
        hits = webstats.gethits(self.file, datetime.date(2016, 12, 31), 1)
        expected = [
            '180.76.5.169',
            '79.56.87.148',
            '79.56.87.148',
            '79.56.87.148',
            '87.10.85.230',
            '87.10.85.230',
            '54.234.72.18',
            '54.234.72.18',
            '95.10.51.244']
        self.assertListEqual(hits, expected)

    def test_radius2(self):
        hits = webstats.gethits(self.file, datetime.date(2016, 12, 31), 2)
        expected = [
            '66.249.73.89',
            '66.249.73.89',
            '180.76.5.195',
            '66.249.73.89',
            '180.76.5.169',
            '79.56.87.148',
            '79.56.87.148',
            '79.56.87.148',
            '87.10.85.230',
            '87.10.85.230',
            '54.234.72.18',
            '54.234.72.18',
            '95.10.51.244']
        self.assertListEqual(hits, expected)


class TestShow(unittest.TestCase):

    def test_no_hits(self):
        with patch('sys.stdout', new=io.StringIO()) as output:
            webstats.show([])
            out = output.getvalue().strip()
            self.assertEqual(out, 'Numero di hit: 0')

    def test_some_hits(self):
        hits = [
            '66.249.73.89',
            '66.249.73.89',
            '180.76.5.195',
            '66.249.73.89',
            '66.249.73.89',
            '79.56.87.148',
            '79.56.87.148',
            '87.10.85.230',
            '79.56.87.148',
            '54.234.72.18',
            '87.10.85.230',
            '95.10.51.244']
        with patch('sys.stdout', new=io.StringIO()) as output:
            webstats.show(hits)
            self.assertEqual(
                output.getvalue(),
                'Numero di hit: %d\n'
                'Visitatori unici: %d\n'
                'Maggior numero di hit:\n'
                '66.249.73.89 -> 4\n'
                '79.56.87.148 -> 3\n'
                '87.10.85.230 -> 2\n' % (len(hits), len(set(hits))))


class TestMain(unittest.TestCase):

    def setUp(self):
        self.old_argv = sys.argv.copy()
        sys.argv.extend(['-f', LOGFILE, '-d', '2016 12 31'])

    def tearDown(self):
        sys.argv = self.old_argv

    def test_main(self):
        with patch('sys.stdout', new=io.StringIO()) as output:
            webstats.main()
            self.assertEqual(
                output.getvalue(),
                'Numero di hit: 2\n'
                'Visitatori unici: 1\n'
                'Maggior numero di hit:\n'
                '87.10.85.230 -> 2\n')


if __name__ == '__main__':
    unittest.main()
