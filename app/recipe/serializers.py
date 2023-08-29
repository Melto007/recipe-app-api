"""
Serializers for recipe apis
"""

from rest_framework import serializers
from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe api"""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'description']
        # extra_kwargs = {'id': {'read_only': True}}
        read_only_fields = ['id']
