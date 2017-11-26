"""movieit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from rest_framework import routers
from .views import *

movie_routers = routers.DefaultRouter()
movie_routers.register(r'users', UserViewSet)
movie_routers.register(r'groups', GroupViewSet)
movie_routers.register(r'partners_data', PartnersDataViewSet)
movie_routers.register(r'rating', RatingViewSet)
movie_routers.register(r'movies', MovieViewSet)
movie_routers.register(r'movie_theathers', MovieTheatherViewSet)
movie_routers.register(r'now_playing', NowPlayingViewSet)