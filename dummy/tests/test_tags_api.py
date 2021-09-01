from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core import models
from dummy.serializers import TagSerializer


TAGS_URL = reverse('dummy:tag-list')


class PublicTagsApiTests(TestCase):
    """test publicly available tags API"""


    def setUp(self) -> None:
        self.client = APIClient()


    def test_login_required(self):
        """test login required"""
        res = self.client.get(TAGS_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagsApiTests(TestCase):
    """test the authorized user tags api"""


    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user('test@gmail.com', 'password1')
        self.client.force_authenticate(self.user)


    def test_retrieve_tags(self):
        """test retrieving tags"""
        models.Tag.objects.create(user=self.user, name='Vegan')
        models.Tag.objects.create(user=self.user, name='Dessert')
        res = self.client.get(TAGS_URL)
        tags = models.Tag.objects.all().order_by('-name')
        serializer = TagSerializer(tags, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)


    def test_tags_limited_to_user(self):
        """test that tags returned are for authenticated user"""
        user2 = get_user_model().objects.create_user('test2@gmail.com', 'password1')
        models.Tag.objects.create(user=user2, name='Fruity')
        tag = models.Tag.objects.create(user=self.user, name='Cola')
        res = self.client.get(TAGS_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], tag.name)
