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
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipe for authenticated user"""
        return Recipe.objects.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return serializer class based on request"""

        if self.action == 'list':
            return serializers.RecipeSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """create new recipe"""
        serializer.save(user=self.request.user)
