"""
views for recipe api
"""

from rest_framework import (
    viewsets,
    authentication,
    permissions
)

from recipe import serializers
from core.models import Recipe


class RecipeViewSets(viewsets.ModelViewSet):
    """viewset for recipe api"""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipe for authenticated user"""
        return Recipe.objects.filter(user=self.request.user).order_by('-id')
