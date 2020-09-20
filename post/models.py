""" IG Post Model """
from django.db import models
from django.conf import settings

class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='Owner',
                              on_delete=models.CASCADE)
    image = models.ImageField('Image',
                              upload_to='post/')
    posted_on = models.DateTimeField(auto_now_add=True)
    caption = models.CharField('Caption', max_length=50, blank=True)
