from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core import models


INGREDIENTS_URL = reverse('dummy:ingredient-list')


class PublicIngredientApiTests(TestCase):
    """test public available apis"""


    def setUp(self):
        self.client = APIClient()


    def test_login_required(self):
        """test login is required to access the endpoint"""
        res = self.client.get(INGREDIENTS_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateIngredientApiTests(TestCase):
    """test private available apis"""


    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@gmail.com',
            'testpass'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_ingredients_list(self):
        """test retrieving a list of inredients"""
        models.Ingredient.objects.create(user=self.user, name='kale')
        models.Ingredient.objects.create(user=self.user, name='salt')
