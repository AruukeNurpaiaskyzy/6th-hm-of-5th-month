from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView

from .models import User
from .serializers import UserSerializer, UserRegisterSerializer, UserDestroySerializer

# Create your views here.
class UserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegisterAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    
class UserDestroyAPI (DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer