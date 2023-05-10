from django.urls import path
from . import views

urlpatterns = [
    path("items", views.itemAPI, name="all_items"),
    path("items/<str:item_id>", views.itemAPI, name="item"),
    path("trinkets", views.trinketAPI, name="all_trinkets"),
    path("trinkets/<str:trinket_id>", views.trinketAPI, name="trinket"),
    path("characters", views.characterAPI, name="all_characters"),
    path("characters/<str:character_id>", views.characterAPI, name="character"),
    path("synergies", views.synergyAPI, name="all_synergies"),
    path("interactions", views.interactionAPI, name="interactions"),
    path("relationships/<str:source>_<str:target>", views.relationshipAPI, name="rel"),
    path("all", views.allAPI, name="all"),
    path("all/names", views.allNamesAPI, name="names"),
    path("all/<str:node1_id>", views.searchAPI, name="search"),
    path("all/rel/<str:rel>", views.searchAPI, name="search"),
    path("all/<str:node1_id>/rel/<str:rel>", views.searchAPI, name="search"),
    path("all/<str:node1_id>/<str:node2_id>", views.searchAPI, name="search"),
    path("all/<str:node1_id>/<str:rel>/<str:node2_id>", views.searchAPI, name="search"),
]
