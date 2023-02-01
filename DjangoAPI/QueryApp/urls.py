from django.urls import path
from . import views

urlpatterns = [
    path("items", views.itemAPI, name="items"),
    path("trinkets", views.trinketAPI, name="trinkets"),
    path("characters", views.characterAPI, name="characters"),
    path("synergies", views.synergyAPI, name="synergies"),
    path("interactions", views.interactionAPI, name="interactions"),
]
