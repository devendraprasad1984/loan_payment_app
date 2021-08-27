from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):


    def test_create_user_with_email_successful(self):
        """test creating new user when email is successful"""
        email = "test@gmail.com"
        pwd = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=pwd
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(pwd))