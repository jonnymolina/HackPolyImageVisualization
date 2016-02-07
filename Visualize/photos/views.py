from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class Setup(APIView):
    def post(self, request, format=None):
        #use SetupSerializer
        return Response({'setupTestkey': 'setupTestvalue'}, status=status.HTTP_200_OK)

class Load(APIView):
    def get(self, request, format=None):
        # use LoadSerializer
        return Response({'loadTestkey': 'loadTestvalue'}, status=status.HTTP_200_OK)

class Clear(APIView):
    def post(self, request, format=None):
        return Response({'clearTestkey': 'clearTestvalue'}, status=status.HTTP_200_OK)