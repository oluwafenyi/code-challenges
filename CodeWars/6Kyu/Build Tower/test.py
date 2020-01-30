import unittest

from tower_builder import tower_builder


class TowerBuilderTest(unittest.TestCase):

    def test_tower_builder(self):
        self.assertEqual(tower_builder(1), ['*', ])
        self.assertEqual(tower_builder(2), [' * ', '***'])
        self.assertEqual(tower_builder(3), ['  *  ', ' *** ', '*****'])


if __name__ == '__main__':
    unittest.main()
