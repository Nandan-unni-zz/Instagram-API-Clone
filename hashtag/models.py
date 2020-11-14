from django.db import models

from post.models import Post
class Hashtag(models.Model):
    name = models.CharField("Name", max_length=500, blank=False, unique=True)
    def related_posts(self):
        return Post.objects.filter(hashtags__id=self.pk)
