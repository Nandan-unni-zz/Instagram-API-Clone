""" Post API views for CRUD and other operations """

# Views and Responses
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (# CreateAPIView,
                                     # ListAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView)

# Django Tools
from django.contrib.auth import get_user_model

# Local Imports
from post.serializers import PostSerializer
from post.models import Post
from user.tests import message


class CreatePostAPI(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        usertags = []
        hashtags = []
        for usertag_pk in data.get('usertags'):
            try:
                usertag = get_user_model().objects.get(pk=usertag_pk)
            except get_user_model().DoesNotExist:
                usertag = None
            if usertag is not None:
                usertags.append(usertag)
        for hashtag_pk in data.get('hashtags'):
            try:
                hashtag = get_user_model().objects.get(pk=hashtag_pk)
            except get_user_model().DoesNotExist:
                hashtag = None
            if hashtag is not None:
                hashtags.append(hashtag)
        try:
            author = get_user_model().objects.get(pk=data.get('author'))
        except get_user_model().DoesNotExist:
            author = None
        if author is not None:
            post = Post(
                author=author,
                image=request.FILES["image"],
                caption=data.get('caption'),
                location=data.get('location'),
                usertags=usertags,
                hashtags=hashtags,
            )
            post.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={"error": "Invalid pk values"})


class GetPostAPI(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class UpdatePostAPI(UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class DeletePostAPI(DestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class LikePostAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            user = get_user_model().objects.get(pk=kwargs['req_user_pk'])
        except get_user_model().DoesNotExist:
            user = None
        try:
            post = Post.objects.get(pk=kwargs['post_pk'])
        except Post.DoesNotExist:
            post = None
        if user is not None and post is not None:
            if user in post.likes.all():
                post.likes.remove(user)
                message(user.username + " unliked the post '{}'".format(post.pk))
            else:
                post.likes.add(user)
                message(user.username + " liked the post '{}'".format(post.pk))
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                        data={"error": "Invalid pk values"})


class SavePostAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            user = get_user_model().objects.get(pk=kwargs['req_user_pk'])
        except get_user_model().DoesNotExist:
            user = None
        try:
            post = Post.objects.get(pk=kwargs['post_pk'])
        except Post.DoesNotExist:
            post = None
        if user is not None and post is not None:
            if user in post.saves.all():
                post.saves.remove(user)
                message(user.username + " unsaved the post '{}'".format(post.pk))
            else:
                post.saves.add(user)
                message(user.username + " saved the post '{}'".format(post.pk))
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                        data={"error": "Invalid pk values"})
