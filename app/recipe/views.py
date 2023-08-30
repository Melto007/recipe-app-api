"""
views for recipe api
"""

from rest_framework import (
    viewsets,
    authentication,
    permissions,
    mixins,
)

from recipe import serializers
from core.models import (
    Recipe,
    Tag,
    Ingredient,
)


class RecipeViewSets(viewsets.ModelViewSet):
    """viewset for recipe api"""
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipe for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return serializer class based on request"""
        if self.action == 'list':
            return serializers.RecipeSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        """create new recipe"""
        serializer.save(user=self.request.user)


class TagViewSets(mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """Viewset for tag"""
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Retrieve tag for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')


class IngredientViewSets(mixins.DestroyModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """viewset for Ingredients model"""
    serializer_class = serializers.IngredientSerializer
    queryset = Ingredient.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Retrieve ingredient for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
