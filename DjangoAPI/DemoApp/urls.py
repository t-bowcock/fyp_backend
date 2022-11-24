from django.urls import path
from . import views

urlpatterns = [path("", views.movieAPI, name="movies")]
