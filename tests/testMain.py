import unittest
import numpy as np
import main

from collections import Counter

class TestUtilsMethods(unittest.TestCase):
    def setUp(self):
        print("SetUp")

    def test_isalpha(self):
        self.assertEqual("a".isalpha(), True)

    def test_isalpha(self):
        self.assertEqual("a".isalpha(), True)

    def test_trans_coverage_no_file(self):
        eCount, nCount = main.trans_coverage_file("no_file.txt")
        print (eCount, nCount)
        self.assertEqual(0, eCount)
        self.assertEqual(0, nCount)

    def test_trans_coverage_file(self):
        eCount, nCount = main.trans_coverage_file("tests/sample.txt")
        print (eCount, nCount)
        self.assertNotEqual(0, eCount)
        self.assertNotEqual(0, nCount)

    def test_trans_coverage_file_kor(self):
        eCount, nCount = main.trans_coverage_file("tests/sample_kor.txt")
        print (eCount, nCount)
        self.assertEqual(0, eCount)
        self.assertNotEqual(0, nCount)

    def test_trans_coverage_file_eng(self):
        eCount, nCount = main.trans_coverage_file("tests/sample_eng.txt")
        print (eCount, nCount)
        self.assertNotEqual(0, eCount)
        self.assertEqual(0, nCount)

    def test_trans_coverage(self):
        eCount, nCount = main.trans_coverage(0, "tests")
        print (eCount, nCount)
        self.assertNotEqual(0, eCount)
        self.assertNotEqual(0, nCount)

if __name__ == '__main__':
    unittest.main()