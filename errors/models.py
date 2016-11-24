from django.db import models
import hashlib

# Create your models here.

class ErrorArt(models.Model):
    artist = models.CharField(max_length=200,help_text="Artist name. Required.",blank=False,unique=True)
    artist_url = models.URLField(help_text="Artist homepage or whatever. Not required.",blank=True)
    slug = models.SlugField(help_text="Long and mystrious auto-generated slug.",blank=False,editable=False,default=False,unique=True)
    content = models.TextField(help_text="The ENTIRE HTML for the page. You'll need to add static assets to the appropriate errors/static/* folder and reference them like src=\"/static/errors/img/[asset].gif\" Required.",blank=False)
    def save(self, *args, **kwargs):
        if self.slug == False:
            # slug is hexdigest of encoded artist name
            artist_enc = str.encode('utf-8')
            self.slug = hashlib.sha224(artist_enc).hexdigest()
        super(ErrorArt, self).save(*args, **kwargs)
    def url(self):
        # returns url string
        return '/' + self.slug
    def __str__(self):
        return self.artist

