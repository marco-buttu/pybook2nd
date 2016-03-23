import unittest
import sys
import os

from importlib import import_module

abspath = os.path.abspath(__file__)
basepath = os.path.dirname(abspath)
suite = unittest.TestSuite()
test_loader = unittest.TestLoader()

for chapter in range(1, 4):
    newpath = '%s/ch%.02d/practice' % (basepath, chapter)
    sys.path.append(newpath)
    module = import_module('tests%.02d' % chapter)
    tests = test_loader.loadTestsFromModule(module)
    suite.addTests(tests)
    sys.path.remove(newpath)

runner = unittest.TextTestRunner()
runner.run(suite)
