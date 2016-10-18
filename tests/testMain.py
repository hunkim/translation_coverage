# -*- coding: utf-8 -*-
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
        e_count, n_count = main.trans_coverage_file("no_file.md")
        print("No file: ", e_count, n_count)
        self.assertEqual(0, e_count)
        self.assertEqual(0, n_count)

    def test_trans_coverage_file(self):
        e_count, n_count = main.trans_coverage_file(
            "tests/sample.md")
        print("sample: ", e_count, n_count)
        self.assertNotEqual(0, e_count)
        self.assertNotEqual(0, n_count)

    def test_trans_coverage_file_kor(self):
        e_count, n_count = main.trans_coverage_file(
            "tests/sample_kor.md")
        print("sample_kor: ", e_count, n_count)
        self.assertEqual(0, e_count)
        self.assertNotEqual(0, n_count)

    def test_trans_coverage_file_eng(self):
        e_count, n_count = main.trans_coverage_file(
            "tests/sample_eng.md")
        print("sample_eng: ", e_count, n_count)
        self.assertNotEqual(0, e_count)
        self.assertEqual(0, n_count)

    def test_trans_coverage_file_source_code(self):
        e_count, n_count = main.trans_coverage_file(
            "tests/sample_source_code.md")
        print("sample_source_code: ", e_count, n_count)
        self.assertEqual(0, e_count)
        self.assertEqual(0, n_count)

    def test_trans_coverage(self):
        args = main.parse_args(["--dir=tests"])
        ext = tuple(args.ext.split())

        e_count, n_count = main.trans_coverage(
            -1, args, "tests", ext)
        print("test dir: ", e_count, n_count)
        self.assertNotEqual(0, e_count)
        self.assertNotEqual(0, n_count)

        # Generate/update sample file
        # `python main.py --dir tests > sample.md`
        with open("sample.md", "r") as sample:
            s1 = sample.read().splitlines()
            s2 = main.print_out(args).splitlines()
            self.assertEqual(s1, s2)

if __name__ == '__main__':
    unittest.main()
