from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import FamilySerializer, UserSerializer
from .models import Family
from rest_framework.response import Response 
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()



# MANAGE GROCERIES
class AllFamilies(APIView):
    def get(self,request):
        try:
            g = Family.objects.all()
            serializer= FamilySerializer(g, many=True)
            return Response(serializer.data) 
        except:
            return Response(status = status.HTTP_204_NO_CONTENT)
    
class ViewFamily(APIView):
    def post(self,request):
        serializer = FamilySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ViewUser(APIView):
    def get(Self,request,username):
        try:
            u = User.objects.get(username = username)
            serializer = UserSerializer(u) 
            return Response(serializer.data)
        except:
            return Response(status = status.HTTP_204_NO_CONTENT)