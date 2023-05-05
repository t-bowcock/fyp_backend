from django.urls import path
from . import views

urlpatterns = [
    path("items", views.itemAPI, name="all_items"),
    path("items/<int:item_id>", views.itemAPI, name="item"),
    path("trinkets", views.trinketAPI, name="all_trinkets"),
    path("trinkets/<int:trinket_id>", views.trinketAPI, name="trinket"),
    path("characters", views.characterAPI, name="all_characters"),
    path("characters/<int:character_id>", views.characterAPI, name="character"),
    path("synergies", views.synergyAPI, name="all_synergies"),
    path("synergies/<str:source>_<str:target>", views.synergyAPI, name="synergy"),
    path("interactions", views.interactionAPI, name="interactions"),
    path("all", views.allAPI, name="all"),
    path("all/names", views.allNamesAPI, name="names"),
]
