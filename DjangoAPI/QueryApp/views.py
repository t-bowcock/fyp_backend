from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from .models import Item, Trinket, Character, SynergyRel, InteractionRel, get_all, get_all_names

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
def characterAPI(request, character_id: int = None):
    if request.method == "GET":

        if character_id is None:
            characters = []
            for character in Character.nodes.all():
                characters.append(character.get_basic())
            return JsonResponse({"characters": characters})

        return JsonResponse(Character.nodes.get(id=character_id).format())


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


def allNamesAPI(request):
    if request.method == "GET":
        return JsonResponse(get_all_names())


def searchAPI(
    request, node1_id: int = None, type1: str = None, rel: str = None, node2_id: int = None, type2: str = None
):
    if request.method == "GET":
        if not node1_id:
            # just query rel
            # need to write a way to rels with nodes, the get_all methods just get the edges
            # probably just use the same CYPER query and format the data differently
            pass
        elif not rel and not node2_id:
            # 1 node
            if type1 == "Item":
                return JsonResponse(Item.nodes.get(id=node1_id).format())
            if type1 == "Trinket":
                return JsonResponse(Trinket.nodes.get(id=node1_id).format())
            if type1 == "Character":
                return JsonResponse(Character.nodes.get(id=node1_id).format())
        elif rel and not node2_id:
            # 1 node and rel
            pass
        elif not rel and node2_id:
            # 2 nodes and no rel
            pass
        elif rel and node2_id:
            # 2 does and rel
            pass
        else:
            # error?
            print("shit")
