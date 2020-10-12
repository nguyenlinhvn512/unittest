import unittest
from letter import LetterCompiler

class TestCompiler(unittest.TestCase):
    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)
    def test_blank(self):
        testcase = ""
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)

unittest.main(argv=['first-arg-is-ignored'], exit=False)
