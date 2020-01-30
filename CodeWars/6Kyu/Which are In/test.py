import unittest

from in_array import in_array


class InArrayTest(unittest.TestCase):

    def test_in_array(self):
        a1 = ["live", "arp", "strong"]
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ['arp', 'live', 'strong']
        self.assertEqual(in_array(a1, a2), r)


if __name__ == '__main__':
    unittest.main()
