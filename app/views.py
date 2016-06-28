from django.shortcuts import render
from rest_framework import generics
from app.models import Movie, Review
from app.serializers import MovieSerializer, ReviewSerializer

# Create your views here.
class MovieListAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
