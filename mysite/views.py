from django.shortcuts import render
from rest_framework import generics
from .models import MyUser
from .serializers import MyUserSerializer


class MyUserView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
