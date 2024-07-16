# views.py
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from .serializers import UserCreateSerializer
User = get_user_model()

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer