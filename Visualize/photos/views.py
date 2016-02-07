from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from photos.models import *
from photos.serializers import *

# Create your views here.
class Setup(APIView):
    def post(self, request, format=None):
        serializer = SetupSerializer(data=request.data)
        #if serializer.is_valid():
        print "serializer is valid"
        rangeNum = serializer.data['rangeNum']
        depth = serlializer.data['depth']
        # get tags from serlializer.url
        tags = ["cat", "cute", "orange", "pet", "kitten"]
        # create Photo model
        photo = Photo(name="cat",
            url=serializer.data['url'],
            tag1=tags[0],
            tag2=tags[1],
            tag3=tags[2],
            tag4=tags[3],
            tag5=tags[4],
            tag6=tags[5])
        # save to db
        photo.save()
        # save the photo model
        return Response({'success': True}, status=status.HTTP_200_OK)
        # use SetupSerializer
        #return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)

class PhotoList(APIView):
    def get(self, request, format=None):
        #return Response(PhotoSerializer(request.user.photo_set.all(), many=True).data)
        return Response(PhotoSerializer(request.user.data))


class Load(APIView):
    def get(self, request, format=None):
        # use LoadSerializer
        return Response({'loadTestkey': 'loadTestvalue'}, status=status.HTTP_200_OK)

class Clear(APIView):
    def post(self, request, format=None):
        return Response({'clearTestkey': 'clearTestvalue'}, status=status.HTTP_200_OK)