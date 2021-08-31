from django.contrib.auth import get_user_model
from django.test import TestCase

from core import models


def sample_user(email='test2@gmail.com', password='test2'):
    return get_user_model().objects.create_user(email, password)


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


    def test_new_user_email_normalize(self):
        """test the email for new user"""
        email = 'devendraprasad1984@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())


    def test_email_new_user_invalid(self):
        """invalid or no email check"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')


    def test_create_new_super_user(self):
        """test creating a new super user"""
        user = get_user_model().objects.create_superuser('test_super_user@gmail.com', 'test123')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


    def test_tag_str(self):
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )
        self.assertEqual(str(tag), tag.name)
