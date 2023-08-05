"""
Unit Test
"""
from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    def test(self):
        res = calc.add(5, 5)
        self.assertEqual(res, 10)

    def test_sub(self):
        res = calc.sub(5, 5)
        self.assertEqual(res, 0)
