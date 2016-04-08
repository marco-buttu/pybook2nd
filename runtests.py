#!/usr/bin/env python

import sys
import unittest
from pathlib import PurePath, Path
from importlib import import_module

suite = unittest.TestSuite()
test_loader = unittest.TestLoader()
rootdir = Path(__file__).parent

for directory in rootdir.glob('ch*'):
    newpath = PurePath(directory.absolute(), Path('practice'))
    pathstr = str(newpath)
    sys.path.append(pathstr)
    module = import_module('tests_%s' % directory.name)
    tests = test_loader.loadTestsFromModule(module)
    suite.addTests(tests)
    sys.path.remove(pathstr)

runner = unittest.TextTestRunner()
runner.run(suite)
