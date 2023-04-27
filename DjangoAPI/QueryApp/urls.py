from django.urls import path
from . import views

urlpatterns = [
    path("items", views.itemAPI, name="all_items"),
    path("items/<str:item_name>", views.itemAPI, name="item"),
    path("trinkets", views.trinketAPI, name="all_trinkets"),
    path("trinkets/<str:trinket_name>", views.trinketAPI, name="trinket"),
    path("characters", views.characterAPI, name="all_characters"),
    path("characters/<str:character_name>", views.characterAPI, name="character"),
    path("synergies", views.synergyAPI, name="all_synergies"),
    path("synergies/<str:source>_<str:target>", views.synergyAPI, name="synergy"),
    path("interactions", views.interactionAPI, name="interactions"),
    path("all", views.allAPI, name="all"),
]
