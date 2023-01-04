from django.urls import path
from . import views

urlpatterns = [path("items", views.itemAPI, name="items")]
