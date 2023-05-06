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
    path("synergies/<str:source>_<str:target>", views.synergyAPI, name="synergy"),
    path("interactions", views.interactionAPI, name="interactions"),
    path("all", views.allAPI, name="all"),
    path("all/names", views.allNamesAPI, name="names"),
    path("all/<str:type1>_<str:node1_id>", views.searchAPI, name="search"),
    path("all/<str:rel>", views.searchAPI, name="search"),
    path("all/<str:type2>_<str:node2_id>", views.searchAPI, name="search"),
    path("all/<str:type1>_<str:node1_id>/<str:rel>", views.searchAPI, name="search"),
    path("all/<str:type1>_<str:node1_id>/<str:type2>_<str:node2_id>", views.searchAPI, name="search"),
    path("all/<str:type1>_<str:node1_id>/<str:rel>/<str:type2>_<str:node2_id>", views.searchAPI, name="search"),
]
