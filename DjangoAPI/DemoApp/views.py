from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse

from .models import Movie, Person


@csrf_exempt
def movieAPI(request):
    if request.method == "GET":
        # Figure how what format this needs to be to processes by front end
        return HttpResponse(Movie.nodes.all())
