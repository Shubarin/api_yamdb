from rest_framework import serializers

from ..models.categories import Category
from ..models.genres import Genre
from ..models.titles import Title

from .genres import GenreSerializer
from .categories import CategorySerializer


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='slug',
                                            queryset=Category.objects.all(),
                                            required=False)
    genre = serializers.SlugRelatedField(slug_field='slug',
                                         queryset=Genre.objects.all(),
                                         many=True)

    class Meta:
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category',)
        model = Title


class TitleListSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category',)
        model = Title
