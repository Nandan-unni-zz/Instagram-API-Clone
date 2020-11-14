from django.db import models
from django.conf import settings

class Comment(models.Model):
    post = models.ForeignKey('post.Post',
                             related_name='Comment_from_Post',
                             on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='Comment_Author',
                               on_delete=models.CASCADE)
    content = models.CharField('Content', max_length=2000, blank=False)
    usertags = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      related_name='Comment_Tags',
                                      blank=True,
                                      symmetrical=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name="Comment_Likes",
                                   blank=True,
                                   symmetrical=False)
    posted_time = models.DateTimeField('Comment_posted_time', auto_now_add=True)

    def __str__(self):
        return "{}'s comment in {}".format(self.author, self.post)

    def likes_count(self):
        if self.likes.count():
            return self.likes.count()
        return 0
