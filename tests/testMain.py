import unittest
import numpy as np
import main

from collections import Counter


class TestUtilsMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_isalpha(self):
        self.assertEqual("a".isalpha(), True)

    def test_trans_coverage_no_file(self):
        e_count, n_count = main.trans_coverage_file("no_file.txt")
        self.assertEqual(0, e_count)
        self.assertEqual(0, n_count)

    def test_trans_coverage_file(self):
        e_count, n_count = main.trans_coverage_file("tests/sample.txt")
        self.assertNotEqual(0, e_count)
        self.assertNotEqual(0, n_count)

    def test_trans_coverage_file_kor(self):
        e_count, n_count = main.trans_coverage_file("tests/sample_kor.txt")
        self.assertEqual(0, e_count)
        self.assertNotEqual(0, n_count)

    def test_trans_coverage_file_eng(self):
        e_count, n_count = main.trans_coverage_file("tests/sample_eng.txt")
        self.assertNotEqual(0, e_count)
        self.assertEqual(0, n_count)

#    def test_trans_coverage(self):
#        e_count, n_count = main.trans_coverage(0, "tests")
#        print (e_count, n_count)
#        self.assertNotEqual(0, e_count)
#        self.assertNotEqual(0, n_count)

if __name__ == '__main__':
    unittest.main()
