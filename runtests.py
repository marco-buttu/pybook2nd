#!/usr/bin/env python

import unittest
import sys
import os

from importlib import import_module

abspath = os.path.abspath(__file__)
basepath = os.path.dirname(abspath)
suite = unittest.TestSuite()
test_loader = unittest.TestLoader()

files = os.listdir(basepath)
chapters = [item for item in files if item.startswith('ch')]
for chapter in chapters:
    newpath = '%s/%s/practice' % (basepath, chapter)
    sys.path.append(newpath)
    module = import_module('tests_%s' % chapter)
    tests = test_loader.loadTestsFromModule(module)
    suite.addTests(tests)
    sys.path.remove(newpath)

runner = unittest.TextTestRunner()
runner.run(suite)
