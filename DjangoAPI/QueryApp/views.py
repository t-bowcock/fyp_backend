from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse

from .models import Item


@csrf_exempt
def itemAPI(request):
    if request.method == "GET":
        # Figure how what format this needs to be to processes by front end
        return HttpResponse(Item.nodes.all())
