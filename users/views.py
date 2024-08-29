from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
# from .permissions import IsAdminUserOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() # Define queryset here
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUserOrReadOnly]

    
