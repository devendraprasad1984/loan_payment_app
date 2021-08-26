from django.test import TestCase

from app.app import calc

class CalcAddTest(TestCase):
    def __test_add_two_numbers(self):
        """add 2 numbers"""
        self.assertEqual(calc.add(8,2),10)

