from app.calculator import add
from django.test import TestCase


class Tests_Calculator(TestCase):


    def test_add(self):
        self.assertEqual(add(2, 3), 5)
