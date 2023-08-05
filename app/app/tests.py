"""
Unit Test
"""

from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    """ Test the calc module """
    def test(self):
        """ Test adding number together """
        res = calc.add(5, 5)

        self.assertEqual(res, 10)

    def test_sub(self):
        """ Test sub number together """
        res = calc.sub(5, 5)

        self.assertEqual(res, 0)
        