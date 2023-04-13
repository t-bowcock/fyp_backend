from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from .models import Item, Trinket, Character, SynergyRel, InteractionRel, get_all

# Pylint cannot find nodes.all() member for some reason
# pylint: disable=no-member


@csrf_exempt
def itemAPI(request):
    if request.method == "GET":
        items = []
        for item in Item.nodes.all():
            items.append(item.get_basic())
        content = {"items": items}
        return JsonResponse(content)


@csrf_exempt
def trinketAPI(request):
    if request.method == "GET":
        trinkets = []
        for trinket in Trinket.nodes.all():
            trinkets.append(trinket.get_basic())
        content = {"trinkets": trinkets}
        return JsonResponse(content)


@csrf_exempt
def characterAPI(request):
    if request.method == "GET":
        characters = []
        for character in Character.nodes.all():
            characters.append(character.get_basic())
        content = {"characters": characters}
        return JsonResponse(content)


@csrf_exempt
def synergyAPI(request):
    if request.method == "GET":
        synergy_rel = SynergyRel()
        synergies = synergy_rel.get_all_basic()
        content = {"synergies": synergies}
        return JsonResponse(content)


@csrf_exempt
def interactionAPI(request):
    if request.method == "GET":
        interaction_rel = InteractionRel()
        interactions = interaction_rel.get_all_basic()
        content = {"interactions": interactions}
        return JsonResponse(content)


@csrf_exempt
def allAPI(request):
    print("all request")
    if request.method == "GET":
        # items = []
        # for item in Item.nodes.all():
        #     items.append(item.get_basic())
        # print("items done")
        # trinkets = []
        # for trinket in Trinket.nodes.all():
        #     trinkets.append(trinket.get_basic())
        # print("trinkets done")
        # characters = []
        # for character in Character.nodes.all():
        #     characters.append(character.get_basic())
        # print("characters done")
        # synergy_rel = SynergyRel()
        # synergies = synergy_rel.get_all_basic()
        # print("synergies done")
        # interaction_rel = InteractionRel()
        # interactions = interaction_rel.get_all_basic()
        # print("interactions done")

        # content = {
        #     "items": items,
        #     "trinkets": trinkets,
        #     "characters": characters,
        #     "synergies": synergies,
        #     "interactions": interactions,
        # }

        # print("sending response")
        # return JsonResponse(content)
        get_all()
