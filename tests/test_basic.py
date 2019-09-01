from context import dmath
import unittest

class TestDualNumbersEquality(unittest.TestCase):

    def test_dual_equals_itself(self):
        self.assertEqual(dmath.dual(3,2), dmath.dual(3,2))

    def test_dual_equals_scalar(self):
        self.assertEqual(dmath.dual(3), 3)

    def test_dual_not_equals_scalar(self):
        self.assertNotEqual(dmath.dual(3,1), 3)

    def test_dual_equals_similar_dual(self):
        self.assertEqual(dmath.dual(3,1), dmath.dual(3,1,0))

    def test_dual_not_equals_longer_dual(self):
        self.assertNotEqual(dmath.dual(3,1), dmath.dual(3,1,1))

class TestDualNumbersAdding(unittest.TestCase):

    def test_adding_of_same_dimension(self):
        self.assertEqual(dmath.dual(3,1) + dmath.dual(4,1), dmath.dual(7,2))

    def test_adding_of_different_length_numbers(self):
        self.assertEqual(dmath.dual(3,1) + dmath.dual(3,1,1), dmath.dual(6,2,1))

    def test_adding_to_scalar(self):
        self.assertEqual(dmath.dual(3,1) + 3, dmath.dual(6,1))
        self.assertEqual(3 + dmath.dual(3,1), dmath.dual(6,1))


if __name__ == '__main__':
    unittest.main()
