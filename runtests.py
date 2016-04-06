#!/usr/bin/env python

import sys
import unittest
from pathlib import Path
from importlib import import_module

suite = unittest.TestSuite()
test_loader = unittest.TestLoader()
rootdir = Path(__file__).parent

for directory in rootdir.glob('ch*'):
    newpath = '%s/practice' % directory.absolute()
    sys.path.append(newpath)
    module = import_module('tests_%s' % directory.name)
    tests = test_loader.loadTestsFromModule(module)
    suite.addTests(tests)
    sys.path.remove(newpath)

runner = unittest.TextTestRunner()
runner.run(suite)
