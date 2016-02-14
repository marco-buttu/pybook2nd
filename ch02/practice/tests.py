import unittest
from digit2word import digit2word, digit2word_2nd


mapping = {0: 'zero', 1: 'uno', 2: 'due', 3: 'tre', 4: 'quattro'}


class TestDigit2Word(unittest.TestCase):

    def test_right_value(self):
        for key, value in mapping.items():
            self.assertEqual(digit2word(key), value)
            self.assertEqual(digit2word_2nd(key), value)

    def test_wrong_value(self):
        """Return 'unknown' in case of wrong value"""
        self.assertEqual(digit2word('pippo'), 'unknown')
        self.assertEqual(digit2word_2nd(5), 'unknown')


if __name__ == '__main__':
    unittest.main()
