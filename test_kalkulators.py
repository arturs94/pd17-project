import unittest
from kalkulators import saskaitit

class TestKalkulators(unittest.TestCase):

    def test_saskaitit_positive(self):
        self.assertEqual(saskaitit(3, 4), 8)

    def test_saskaitit_zero(self):
        self.assertEqual(saskaitit(0, 0), 0)

    def test_saskaitit_negative(self):
        self.assertEqual(saskaitit(-2, -5), -7)

    def test_saskaitit_mixed(self):
        self.assertEqual(saskaitit(-3, 5), 2)

if __name__ == "__main__":
    unittest.main()
