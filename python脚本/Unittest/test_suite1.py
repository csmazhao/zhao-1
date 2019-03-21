# -*- coding: utf-8 -*-

import unittest
from test_mathfunc import TestMathFunc

if __name__ == '__main__':

    suite = unittest.TestSuite()
    tests = [unittest.TestLoader().loadTestsFromNames(
        ['test_mathfunc.TestMathFunc.test_multi', 'test_mathfunc.TestMathFunc.test_minus' \
            , 'test_mathfunc.TestMathFunc.test_add', 'test_mathfunc.TestMathFunc.test_divide'])]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)