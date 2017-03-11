import os
import types
import unittest
from ch14.practice import file_finder_gen, file_finder_list

DIR = os.path.join(os.path.dirname(file_finder_gen.__file__), 'mydir')


class FileFinderGenTestCase(unittest.TestCase):

    def test_py_extension(self):
        g = file_finder_gen.file_finder('*.py', DIR)
        self.assertTrue(isinstance(g, types.GeneratorType))
        expected = [
            os.path.join(DIR, 'file1.py'),
            os.path.join(DIR, 'file2.py'),
            os.path.join(DIR, 'file3.py')]
        self.assertListEqual(sorted(list(g)), expected)


class FileFinderListTestCase(unittest.TestCase):

    def test_py_extension(self):
        result = file_finder_list.file_finder('*.py', DIR)
        self.assertTrue(isinstance(result, list))
        expected = [
            os.path.join(DIR, 'file1.py'),
            os.path.join(DIR, 'file2.py'),
            os.path.join(DIR, 'file3.py')]
        self.assertListEqual(sorted(result), expected)



if __name__ == '__main__':
    unittest.main()
