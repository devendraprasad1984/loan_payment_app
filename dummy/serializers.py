from rest_framework import serializers

from core import models


class TagSerializer(serializers.ModelSerializer):
    """serializer for tag objects"""


    class Meta:
        model = models.Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)
