from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from .models import Item, Trinket, Character, SynergyRel, InteractionRel, get_all, get_all_names, custom_query, get_rel

# Pylint cannot find nodes.all() member for some reason
# pylint: disable=no-member


@csrf_exempt
def itemAPI(request, item_id: str = None):
    if request.method == "GET":
        if item_id is None:
            return JsonResponse({"items": Item.get_all()})

        return JsonResponse(Item.get(item_id))


@csrf_exempt
def trinketAPI(request, trinket_id: str = None):
    if request.method == "GET":
        if trinket_id is None:
            return JsonResponse({"trinkets": Trinket.get_all()})

        return JsonResponse(Trinket.get(trinket_id))


@csrf_exempt
def characterAPI(request, character_id: str = None):
    if request.method == "GET":
        if character_id is None:
            return JsonResponse({"characters": Character.get_all()})

        return JsonResponse(Character.get(character_id))


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
def relationshipAPI(request, source: str, target: str):
    if request.method == "GET":
        return JsonResponse(get_rel(source, target))


@csrf_exempt
def allAPI(request):
    if request.method == "GET":
        return JsonResponse(get_all())


@csrf_exempt
def allNamesAPI(request):
    if request.method == "GET":
        return JsonResponse(get_all_names())


@csrf_exempt
def searchAPI(request, node1_id: str = None, rel: str = None, node2_id: str = None):
    if request.method == "GET":
        query = ""
        print(rel)
        if not node1_id and rel:
            print("???")
            query = f"MATCH (n)-[r:{rel}]-(m) RETURN n.id, n.name, labels(n), m.id, m.name, labels(m)"
        elif not rel and not node2_id:
            # 1 node
            query = f"MATCH (n{{id:'{node1_id}'}})-[r]-(m) RETURN n.id, n.name, labels(n), m.id, m.name, labels(m)"
        elif rel and not node2_id:
            # 1 node and rel
            query = (
                f"MATCH (n{{id:'{node1_id}'}})-[r:{rel}]-(m) RETURN n.id, n.name, labels(n), m.id, m.name, labels(m)"
            )
        elif not rel and node2_id:
            # 2 nodes and no rel
            query = f"MATCH (n{{id:'{node1_id}'}})-[r]-(m{{id:'{node2_id}'}}) RETURN n.id, n.name, labels(n), m.id, m.name, labels(m)"
        elif rel and node2_id:
            # 2 does and rel
            query = f"MATCH (n{{id:'{node1_id}'}})-[r:{rel}]-(m{{id:'{node2_id}'}}) RETURN n.id, n.name, labels(n), m.id, m.name, labels(m)"
        return JsonResponse(custom_query(query))
