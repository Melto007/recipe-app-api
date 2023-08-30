"""
Serializers for recipe apis
"""

from rest_framework import serializers
from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe api"""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        # extra_kwargs = {'id': {'read_only': True}}
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for details view"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
