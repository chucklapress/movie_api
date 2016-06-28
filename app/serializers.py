from rest_framework import serializers
from app.models import Movie, Review




class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id','movie_title','release_date','video_release_date','IMBd_URL','unknown','action','adventure','animation','childrens','comedy', 'crime','documentary','drama','fantasy','film_noir','horror','musical','mystery','romance','sci_fi','thriller','war','western')

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('rater','movie','rating','timestamp')
