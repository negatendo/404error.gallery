from django.shortcuts import render
from django.http import HttpResponse
from .models import ErrorArt

def index(request):
    return HttpResponse("Hello, world. You're at the error index. This page will soon list all Error art entries.")

def display(request, slug):
    try:
        error_art = ErrorArt.objects.get(slug=slug)
    except:
        return HttpResponse('Didnt find that page so show a random ErrorArt here!',status=404)
    # render raw content of object found!
    return HttpResponse(error_art.content,status=404)

