from rest_framework import serializers
from django.contrib.auth import get_user_model

from post.models import Post

class CreateUserSerializer(serializers.ModelSerializer):
    ''' Serializer of creating user '''
    class Meta:
        model = get_user_model()
        fields = ['email', 'full_name', 'username', 'birthday', 'password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class MiniUserSerializer(serializers.ModelSerializer):
    ''' Mini version of User Serializer '''
    class Meta:
        model = get_user_model()
        fields = ['pk', 'username', 'full_name', 'profile_pic']


class PostSerializer(serializers.ModelSerializer):
    author = MiniUserSerializer(many=True)
    likes = MiniUserSerializer(many=True)
    tags = MiniUserSerializer(many=True)
    class Meta:
        model = Post
        fields = ['pk', 'author', 'image', 'caption', 'location',
                  'likes', 'likes_count', 'tags']


class PublicUserSerializer(serializers.ModelSerializer):
    ''' Serializer for R operaton '''
    followers = MiniUserSerializer(many=True)
    following = MiniUserSerializer(many=True)
    posts = PostSerializer(many=True)
    tagged_posts = PostSerializer(many=True)
    class Meta:
        model = get_user_model()
        fields = ['pk', 'full_name', 'username',
                  'profile_pic', 'website', 'bio',
                  'followers', 'followers_count',
                  'following', 'following_count',
                  'posts', 'post_count',
                  'tagged_posts']


class PrivateUserSerializer(serializers.ModelSerializer):
    ''' Serializer for R operaton '''
    class Meta:
        model = get_user_model()
        fields = ['pk', 'full_name', 'username',
                  'profile_pic', 'website', 'bio',
                  'followers_count', 'following_count', 'post_count']


class MyProfileSerializer(serializers.ModelSerializer):
    ''' Serializer for RUD operatons '''
    followers = MiniUserSerializer(many=True)
    following = MiniUserSerializer(many=True)
    posts = PostSerializer(many=True)
    tagged_posts = PostSerializer(many=True)
    saved_posts = PostSerializer(many=True)
    class Meta:
        model = get_user_model()
        fields = ['pk', 'full_name', 'email', 'username', 'ph_number',
                  'birthday', 'profile_pic', 'website', 'bio',
                  'followers', 'followers_count',
                  'following', 'following_count',
                  'posts', 'post_count',
                  'tagged_posts', 'saved_posts']


class UploadUserPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['profile_pic']
