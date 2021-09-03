from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core import models
from dummy import serializers


class TagViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    """manage tags in databse"""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer


    def get_queryset(self):
        """get tag for logged in user"""
        return self.queryset.filter(self.request.user).order_by('-name')


    def perform_create(self, serializer):
        """create a new tag"""
        serializer.save(user=self.request.user)
