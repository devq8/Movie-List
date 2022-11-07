from rest_framework import serializers
from movies.models import Movie, List

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description',]

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['user', 'movies',]