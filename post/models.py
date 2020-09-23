""" IG Post Model """
from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='Owner',
                              on_delete=models.CASCADE)
    image = models.ImageField('Image',
                              upload_to='post/')
    posted_on = models.DateTimeField(auto_now_add=True)
    caption = models.CharField('Caption', max_length=50, blank=True)
    location = models.CharField('Location', max_length=30, blank=True)
    tag = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                 related_name='Tagged User',
                                 on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name="Likes",
                                   blank=True,
                                   symmetrical=False)
    saves = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name="Saves",
                                   blank=True,
                                   symmetrical=False)

    def __str__(self):
        return self.author.username + ' ({})'.format(self.pk)

    def likes_count(self):
        if self.likes.count():
            return self.likes.count()
        return 0
