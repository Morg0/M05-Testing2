#import unittest
import unittest
#from the my_sum folder get the sum
from my_sum import sum
from fractions import Fraction

#a class called TestSum with unittest
class TestSum(unittest.TestCase):
    #defines a test medtod to test a list of integers
    def test_list_init(self):
        """
        Test that it can sum a list of intergers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()        