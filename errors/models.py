from django.db import models

# Create your models here.

class ErrorArt(models.Model):
    title = models.CharField(max_length=200,help_text="The title as it appears on our homepage list. Not required.",blank=True)
    artist = models.CharField(max_length=200,help_text="Artist name. Required.",blank=False)
    artist_url = models.URLField(help_text="Artist homepage or whatever. Not required.",blank=True)
    slug = models.SlugField(help_text="The part of the URL we want to be able to link this 404 error from, without the slash. Ex: A value of 'my-404-page' would resolve to http://404error.gallery/my-404-page. Required.",blank=False)
    content = models.TextField(help_text="The ENTIRE HTML for the page. You'll need to add static assets to the appropriate errors/static/* folder and reference them like src=\"/static/errors/img/[asset].gif\" Required.",blank=False)
    def __str__(self):
        return self.artist
