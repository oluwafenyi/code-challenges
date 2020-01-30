import unittest

from find_it import find_it


class FindItTest(unittest.TestCase):

    def test_find_it(self):
        self.assertEqual(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20,
                                 4, -1, -2, 5]), 5)


if __name__ == "__main__":
    unittest.main()
