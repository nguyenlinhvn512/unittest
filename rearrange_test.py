import unittest
from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Khanh Linh, Nguyen"
        expected = "Nguyen Khanh Linh"
        self.assertEqual(rearrange_name(testcase),expected)
    
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase),expected)

    def test_double_name(self):
        testcase = "Linh, Nguyen K."
        expected = "Nguyen K. Linh"
        self.assertEqual(rearrange_name(testcase),expected)

    def test_one_name(self):
        testcase = "Linh"
        expected = "Linh"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_invalid_type_name(self):
        self.assertRaises(TypeError, rearrange_name, 10)

unittest.main()