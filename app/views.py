from django.shortcuts import render
from rest_framework import generics
from app.models import Movie, Review, Rater
from app.serializers import MovieSerializer, ReviewSerializer, RaterSerializer

# Create your views here.

class MovieListAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RaterListAPIView(generics.ListCreateAPIView):
    queryset = Rater.objects.all()
    serializer_class = RaterSerializer

class RaterDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rater.objects.all()
    serializer_class = RaterSerializer
