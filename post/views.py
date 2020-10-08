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
        tags = []
        for tag_pk in data.get('tags'):
            try:
                tag = get_user_model().objects.get(pk=tag_pk)
            except get_user_model().DoesNotExist:
                tag = None
            if tag is not None:
                tags.append(tag)
        post = Post(
            author=get_user_model().objects.get(pk=data.get('author')),
            image=request.FILES["image"],
            caption=data.get('caption'),
            location=data.get('location')
        )
        post.save()
        return Response(status=status.HTTP_201_CREATED)


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
