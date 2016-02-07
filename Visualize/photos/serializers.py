from rest_framework import serializers
from photos.models import *

class PhotoSerializer(serializers.Serializer):
    url = serializers.TextField(validators=[URLValidator()])
    rangeNum = serializers.IntegerField()
    depth = serializers.IntegerField()

class LoadSerializer(serializers.Serializer):
    url = serializers.TextField(validators=[URLValidator()])