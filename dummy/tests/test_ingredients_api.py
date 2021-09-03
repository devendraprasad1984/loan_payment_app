from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core import models
from dummy import serializers


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


    def test_retrieve_ingredient_list(self):
        """Test retrieving a list of ingredients"""
        models.Ingredient.objects.create(user=self.user, name='kale')
        models.Ingredient.objects.create(user=self.user, name='Salt')

        res = self.client.get(INGREDIENTS_URL)

        ingredients = models.Ingredient.objects.all().order_by('-name')
        serializer = serializers.IngredientSerializer(ingredients, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)


    def test_ingredients_limited_to_user(self):
        """Test that only ingredients for authenticated user are returned"""
        user2 = get_user_model().objects.create_user(
            'other@londonappdev.com',
            'testpass'
        )
        models.Ingredient.objects.create(user=user2, name='Vinegar')
        ingredient = models.Ingredient.objects.create(user=self.user, name='Tumeric')
        res = self.client.get(INGREDIENTS_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], ingredient.name)
