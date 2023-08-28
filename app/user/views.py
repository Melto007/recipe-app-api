"""
views for user api
"""

from rest_framework import generics
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """View for creating new user"""
    serializer_class = UserSerializer
