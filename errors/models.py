from django.db import models
from django.conf import settings
import hashlib

# Create your models here.

class ErrorArt(models.Model):
    artist = models.CharField(max_length=200,help_text="Artist name. Required.",blank=False,unique=True)
    artist_url = models.URLField(help_text="Artist homepage or whatever. Not required.",blank=True)
    slug = models.SlugField(help_text="Long and mystrious auto-generated slug. This is the 'URL' for this page, and the directory where its assets will be uploaded.",blank=False,default='',unique=True)
    content = models.TextField(help_text="The ENTIRE HTML for the page. You'll need to reference static assets like src=\"/media/[slug]/[asset].gif\" SAVE THIS RECORD FIRST TO UPLOAD FILES AND SEE THE SLUG. Then change the HTML. Yea it's silly. Required.",blank=False)

    # fetch gallery mode setting for textbox
    if settings.GALLERY_MODE:
        gmode = "Enabled"
    else:
        gmode = "Disabled"
    show_in_gallery_mode = models.BooleanField(default=1,help_text="Uncheck to hide when Gallery Mode is enabled. Gallery Mode is currently: <strong>%s</strong>" % (gmode))
    def save(self, *args, **kwargs):
        if self.slug == '':
            # slug is hexdigest of encoded artist name
            artist_enc = self.artist.encode('utf-8')
            self.slug = hashlib.sha224(artist_enc).hexdigest()
        super(ErrorArt, self).save(*args, **kwargs)
    def url(self):
        # returns url string
        return '/' + self.slug
    def __str__(self):
        return self.artist

class ErrorArtFile(models.Model):
    def get_slug_path(instance,filename):
        return instance.error_art.slug + '/' + filename

    error_art = models.ForeignKey(ErrorArt)
    my_file = models.FileField(upload_to=get_slug_path)

    def __str__(self):
        return '/media/' + self.my_file.name


    def url(self):
        # returns url string
        return '/media/' + self.my_file.url
