import unittest
import argparse

import main


class TestUtilsMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_isascii(self):
        self.assertEqual(main.is_ascii('c'), True)
        self.assertEqual(main.is_ascii('1'), True)
        self.assertEqual(main.is_ascii(' '), True)
        self.assertEqual(main.is_ascii('.'), True)
        self.assertEqual(main.is_ascii('\n'), True)

        self.assertEqual(main.is_ascii('한'), False)
        self.assertEqual(main.is_ascii('金'), False)

    def test_trans_coverage_no_file(self):
        e_count, n_count = main.trans_coverage_file("no_file.txt")
        print("No file: ", e_count, n_count)
        self.assertEqual(0, e_count)
        self.assertEqual(0, n_count)

    def test_trans_coverage_file(self):
        e_count, n_count = main.trans_coverage_file("tests/sample.txt")
        print("sample: ", e_count, n_count)
        self.assertNotEqual(0, e_count)
        self.assertNotEqual(0, n_count)

    def test_trans_coverage_file_kor(self):
        e_count, n_count = main.trans_coverage_file("tests/sample_kor.txt")
        print("sample_kor: ", e_count, n_count)
        self.assertEqual(0, e_count)
        self.assertNotEqual(0, n_count)

    def test_trans_coverage_file_eng(self):
        e_count, n_count = main.trans_coverage_file("tests/sample_eng.txt")
        print("sample_eng: ", e_count, n_count)
        self.assertNotEqual(0, e_count)
        self.assertEqual(0, n_count)

    def test_trans_coverage(self):
        args = main.parse_args(["--dir=tests"])

        e_count, n_count = main.trans_coverage(0, args, "tests")
        print ("test dir: ", e_count, n_count)
        self.assertNotEqual(0, e_count)
        self.assertNotEqual(0, n_count)

if __name__ == '__main__':
    unittest.main()
