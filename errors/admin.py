from django.contrib import admin
from .models import ErrorArt

@admin.register(ErrorArt)
class ErrorArtAdmin(admin.ModelAdmin):
    # list view
    list_display = (
            'artist',
            'url')
    # read only fields
    readonly_fields = ('slug',)
