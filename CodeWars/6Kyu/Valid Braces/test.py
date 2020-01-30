import unittest

from valid_braces import validBraces


class ValidBracesTest(unittest.TestCase):

    def test_valid_braces(self):
        self.assertTrue(validBraces("()"))
        self.assertFalse(validBraces("[(])"))
        self.assertTrue(validBraces("(){}[]"))
        self.assertTrue(validBraces("([{}])"))
        self.assertTrue(validBraces("{}({})[]"))


if __name__ == '__main__':
    unittest.main()
