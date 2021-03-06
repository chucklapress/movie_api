"""movieapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import MovieListAPIView, ReviewListAPIView, RaterListAPIView, MovieDetailAPIView, ReviewDetailAPIView, RaterDetailAPIView, IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^movies/$', MovieListAPIView.as_view(), name="movie_list_api_view"),
    url(r'^movies/(?P<pk>\d+)/$', MovieDetailAPIView.as_view(), name="movie_detail_api_view"),
    url(r'^reviews/$', ReviewListAPIView.as_view(), name="review_list_api_view"),
    url(r'^reviews/(?P<pk>\d+)/$', ReviewDetailAPIView.as_view(), name="review_detail_api_view"),
    url(r'^raters/$', RaterListAPIView.as_view(), name="rater_list_api_view"),
    url(r'^raters/(?P<pk>\d+)/$', RaterDetailAPIView.as_view(), name="rater_detail_api_view")

]
