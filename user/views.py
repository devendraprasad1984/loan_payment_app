from rest_framework import generics

from user import serializers


class CreateUserView(generics.CreateAPIView):
    """create new user in the system"""
    serializer_class = serializers.UserSerializer
