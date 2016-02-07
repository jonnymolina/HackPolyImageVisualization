from rest_framework import serializers
from photos.models import *

class PhotoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    url = serializers.CharField(max_length=500)
    tag1 = serializers.CharField(max_length=50, allow_blank=True)
    tag2 = serializers.CharField(max_length=50, allow_blank=True)
    tag3 = serializers.CharField(max_length=50, allow_blank=True)
    tag4 = serializers.CharField(max_length=50, allow_blank=True)
    tag5 = serializers.CharField(max_length=50, allow_blank=True)
    tag6 = serializers.CharField(max_length=50, allow_blank=True)

class SetupSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=500)
    rangeNum = serializers.IntegerField()
    depth = serializers.IntegerField()

class LoadSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=500)