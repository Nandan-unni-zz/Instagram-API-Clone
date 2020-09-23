from rest_framework import serializers
from post.models import Post
from django.contrib.auth import get_user_model

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['image', 'caption', 'loaction', 'tag']

class PostAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['pk', 'username', 'full_name']

class PostSerializer(serializers.ModelSerializer):
    author = PostAuthorSerializer()
    likes = PostAuthorSerializer(many=True)
    saves = PostAuthorSerializer(many=True)
    tags = PostAuthorSerializer(many=True)
    class Meta:
        model = Post
        fields = ['pk', 'author', 'image', 'caption', 'location',
                  'likes', 'no_of_likes',
                  'saves', 'tags']
