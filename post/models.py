""" IG Post Model """
from django.db import models
from django.conf import settings

from comment.models import Comment

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='Owner',
                               on_delete=models.CASCADE)
    image = models.ImageField('Image',
                              upload_to='post/')
    posted_time = models.DateTimeField('Post_posted_time', auto_now_add=True)
    caption = models.CharField('Caption', max_length=50, blank=True)
    location = models.CharField('Location', max_length=30, blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name="Post_Likes",
                                   blank=True,
                                   symmetrical=False)
    saves = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name="Post_Saves",
                                   blank=True,
                                   symmetrical=False)
    usertags = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      related_name='Post_Tags',
                                      blank=True,
                                      symmetrical=True)
    hashtags = models.ManyToManyField('hashtag.Hashtag',
                                      related_name='Post_Hashags',
                                      blank=True,
                                      symmetrical=True)

    def __str__(self):
        return "{}'s post({})".format(self.author, self.pk)

    def comments(self):
        ''' Get all comments '''
        return Comment.objects.filter(post__id=self.pk)

    def likes_count(self):
        if self.likes.count():
            return self.likes.count()
        return 0
