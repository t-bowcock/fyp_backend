from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from .models import Item, Trinket, Character, SynergyRel, InteractionRel, get_all

# Pylint cannot find nodes.all() member for some reason
# pylint: disable=no-member


@csrf_exempt
def itemAPI(request, item_id: int = None):
    if request.method == "GET":

        if item_id is None:
            items = []
            for item in Item.nodes.all():
                items.append(item.format())
            return JsonResponse({"items": items})

        print(item_id)
        print(Item.nodes.get(id=item_id))
        return JsonResponse(Item.nodes.get(id=item_id).format())


@csrf_exempt
def trinketAPI(request, trinket_id: int = None):
    if request.method == "GET":

        if trinket_id is None:
            trinkets = []
            for trinket in Trinket.nodes.all():
                trinkets.append(trinket.format())
            return JsonResponse({"trinkets": trinkets})

        return JsonResponse(Trinket.nodes.get(id=trinket_id).format())


@csrf_exempt
def characterAPI(request, character_name: str = None):
    if request.method == "GET":

        if character_name is None:
            characters = []
            for character in Character.nodes.all():
                characters.append(character.get_basic())
            return JsonResponse({"characters": characters})

        return JsonResponse(Character.nodes.get(name=character_name).format())


@csrf_exempt
def synergyAPI(request, source: str = None, target: str = None):
    if request.method == "GET":

        if source is None or target is None:
            return JsonResponse({"synergies": SynergyRel.get_all()})

        return JsonResponse(SynergyRel.get(source, target))


@csrf_exempt
def interactionAPI(request, source: str = None, target: str = None):
    if request.method == "GET":

        if source is None or target is None:
            return JsonResponse({"interactions": InteractionRel.get_all()})

        return JsonResponse(InteractionRel.get(source, target))


@csrf_exempt
def allAPI(request):
    if request.method == "GET":
        return JsonResponse(get_all())
