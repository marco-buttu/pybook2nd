import unittest
from bytelen import bytelen
from myformat import myformat

class TestBytelen(unittest.TestCase):

    def test_bytelen_utf(self):
        self.assertEqual(bytelen('è', 'latin-1'), 1)
        self.assertEqual(bytelen('è', 'utf-8'), 2)
        self.assertEqual(bytelen('è', 'utf-16'), 4)
        self.assertEqual(bytelen('è', 'utf-32'), 8)
        self.assertEqual(bytelen('ciao', 'ascii'), 4)
        self.assertEqual(bytelen('ciao', 'utf8'), 4)
        self.assertEqual(bytelen('ciao', 'utf-16'), 10)
        self.assertEqual(bytelen('ciao', 'utf-32'), 20)

class TestMyformat(unittest.TestCase):

    def test_no_separtor(self):
        self.assertEqual(myformat(33, 4), '33.0000')
        self.assertEqual(myformat(33, 0), '33')

    def test_separtor(self):
        self.assertEqual(myformat(1000, 4), '1,000.0000')
        self.assertEqual(myformat(1000, 0), '1,000')
        self.assertEqual(myformat(1000000, 4), '1,000,000.0000')
        self.assertEqual(myformat(1000000, 0), '1,000,000')


if __name__ == '__main__':
    unittest.main()
