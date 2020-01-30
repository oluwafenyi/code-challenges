import unittest

from find_missing_letter import find_missing_letter


class FindTest(unittest.TestCase):

    def test_find_missing_letter(self):
        self.assertEqual(find_missing_letter(['a', 'b', 'c', 'd', 'f']), 'e')
        self.assertEqual(find_missing_letter(['O', 'Q', 'R', 'S']), 'P')


if __name__ == "__main__":
    unittest.main()
