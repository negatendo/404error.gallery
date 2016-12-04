from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import ErrorArt
import random
from coolname import generate_slug as generate_random_slug
from django.views.decorators.cache import cache_page

def index(request):
    random_error_art_list = get_error_arts_as_list()
    random.shuffle(random_error_art_list)
    random_slug = generate_random_slug()
    return render(request,'errors/index.html', { 'arts': random_error_art_list, 'random_slug': random_slug } )

# cache these pages so we go light on the lookup
@cache_page(settings.CACHE_TIME)
def display(request, slug):
    try:
        error_art = ErrorArt.objects.get(slug=slug)
    except:
        # sqllite is not hearty so lets have python do randomizing
        random_error_art_list = get_error_arts_as_list()
        random.shuffle(random_error_art_list)
        return HttpResponse(random_error_art_list[0].content,status=404)
    # render raw content of object found!
    return HttpResponse(error_art.content,status=404)

def get_error_arts_as_list():
    if settings.GALLERY_MODE:
        error_art_list = ErrorArt.objects.all().filter(show_in_gallery_mode=True)
    else:
        error_art_list = ErrorArt.objects.all()
    return list(error_art_list)

def custom_page_not_found(request):
    # all 404 conditions see random 404 art
    random_error_art_list = get_error_arts_as_list()
    random.shuffle(random_error_art_list)
    return HttpResponse(random_error_art_list[0].content,status=404)
