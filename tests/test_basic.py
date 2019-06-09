from context import dmath
import unittest

class TestDualNumbers(unittest.TestCase):

    def setUp(self):
        self.a = dmath.dual(3,2)
        self.A = dmath.dual(3,2,0)
        self.b = dmath.dual(3,1)

    def test_3_2_equals_3_2_0(self):
        self.assertEqual(dmath.dual(3,2), dmath.dual(3,2,0))

    def test_number_equal_to_itself(self):
        self.assertEqual(dmath.dual(3,2), dmath.dual(3,2))

    def test_unequal(self):
        self.assertEqual(dmath.dual(3,2), dmath.dual(2,3))

    def test_equality(self):
        #a dual number is equal to itself
        self.assertEqual(self.a, self.a)

        #a dual number is equal to a copy of itself
        self.assertEqual(self.a, dmath.dual(3,2))

        #a dual number is equal to a dual number with additional zero infinitesimal parts
        self.assertEqual(self.a, self.A)

        #a dual number is not equal to another dual number
        self.assertNotEqual(self.a, self.b)

        #a dual number is equal to a scalar
        self.assertEqual(dmath.dual(3,0,0), 3)

        #a dual number is not equal to a scalar
        self.assertNotEqual(dmath.dual(4,0,0), 3)

        #a dual number is not equal to a scalar
        self.assertNotEqual(dmath.dual(3,1), 3)

    def test_addition(self):
        self.assertEqual(dmath.dual(3) + dmath.dual(2,1), dmath.dual(5,1))
        self.assertEqual(dmath.dual(3,1) + 4, dmath.dual(7,1))
        self.assertEqual(4 + dmath.dual(3,1), dmath.dual(7,1))

if __name__ == '__main__':
    unittest.main()
