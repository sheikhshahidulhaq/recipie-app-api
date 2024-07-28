"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    """Taset the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5,6)

        self.assertEqual(res,11)

    def tset_subtract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(10,15)

        self.assertEqual(res, 5)