from django.shortcuts import render
from django.http import HttpResponse
from .models import ErrorArt

def index(request):
    error_art_list = ErrorArt.objects.order_by('?')
    return render(request,'errors/index.html', { 'arts':error_art_list } )

def display(request, slug):
    try:
        error_art = ErrorArt.objects.get(slug=slug)
    except:
        random_error_art = ErrorArt.objects.order_by('?')[0]
        return HttpResponse(random_error_art.content,status=404)
    # render raw content of object found!
    return HttpResponse(error_art.content,status=404)

