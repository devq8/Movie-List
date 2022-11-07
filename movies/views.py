from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie, List
from movies.serializer import MovieListSerializer, WatchListSerializer

class MoviesListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    
class WatchListView(ListAPIView):
    queryset = List.objects.all()
    serializer_class = WatchListSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    lookup_url_kwarg = 'user_id'
