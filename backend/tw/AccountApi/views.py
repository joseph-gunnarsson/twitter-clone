import re
from sre_constants import SUCCESS
from django.http import request
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .serializers import SignUpUserSerializer,LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class createAccount(APIView):
    def post(self,request):
        user=request.data
        user=SignUpUserSerializer(data=user)
        if user.is_valid():
            user.save()
        else:
            return Response(user.errors)
        return Response({"SUCCESS":"User created"})


class updateUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        print(request.data)
        request.user.set_password(request.data["password"])
        return Response("Updated")
        


class Login(APIView):
    def get(self,request):
        token=request.META.get('HTTP_AUTHORIZATION').replace("Token ","")
        print(token)
        try:
            Token.objects.get(key=token)
            return Response({"SUCCESS":"User exists"}) 
        except:
            return  Response({"Failure":"User do not exists"}) 
        

    def post(self,request):
        ser=LoginSerializer(data=request.data)
        if ser.is_valid():
            user=ser.getUser()
            token=Token.objects.get(user=user)
            token.delete()
            token=Token.objects.create(user=user)
            response={"token":token.key,"username":user.get_username()}
            return Response(response)
        else:
            return Response(ser.errors,status=404)

class updateFollowers(APIView):
    class post(self,request):
        



