from django.db import models
import hashlib

# Create your models here.

class ErrorArt(models.Model):
    artist = models.CharField(max_length=200,help_text="Artist name. Required.",blank=False,unique=True)
    artist_url = models.URLField(help_text="Artist homepage or whatever. Not required.",blank=True)
    slug = models.SlugField(help_text="Long and mystrious auto-generated slug. This is the 'URL' for this page, and the directory where its assets will be uploaded.",blank=False,default='',unique=True)
    content = models.TextField(help_text="The ENTIRE HTML for the page. You'll need to reference static assets like src=\"/[slug]/[asset].gif\" You might need to save this once to see the slug. Required.",blank=False)
    def save(self, *args, **kwargs):
        if self.slug == '':
            # slug is hexdigest of encoded artist name
            artist_enc = str.encode('utf-8')
            self.slug = hashlib.sha224(artist_enc).hexdigest()
        super(ErrorArt, self).save(*args, **kwargs)
    def url(self):
        # returns url string
        return '/' + self.slug
    def __str__(self):
        return self.artist

