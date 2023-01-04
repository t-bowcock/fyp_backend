import json
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, JsonResponse

from .models import Item


@csrf_exempt
def itemAPI(request):
    if request.method == "GET":
        items = []
        for item in Item.nodes.all():
            items.append(item.get())
        content = {"items": items}
        return JsonResponse(content)
