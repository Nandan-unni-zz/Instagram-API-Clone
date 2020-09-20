""" User API views for CRUD and other operations """

# Views and Responses
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.views import APIView

from django.contrib.auth import get_user_model

from user.serializers import CreateUserSerializer, UserSerializer
from user.tests import message

class CreateUserAPI(APIView):
    ''' Create User '''
    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.full_name = user.full_name.title()
            user.save()
            message(user.username + ' created an account.')
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, data=serializer.errors)


class GetUserAPI(RetrieveAPIView):
    ''' Get User '''
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class UpdateUserAPI(UpdateAPIView):
    ''' Update User '''
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class FollowUserAPI(APIView):
    ''' Follow User '''
    def get(self, request, *args, **kwargs):
        req_user = get_user_model().objects.get(pk=kwargs['req_user_pk'])
        ig_user = get_user_model().objects.get(pk=kwargs['ig_user_pk'])
        if req_user in ig_user.followers.all():
            ig_user.followers.remove(req_user)
            req_user.following.remove(ig_user)
            message(req_user.username + ' unfollowed ' + ig_user.username)
        else:
            ig_user.followers.add(req_user)
            req_user.following.add(ig_user)
            message(req_user.username + ' followed ' + ig_user.username)
        return Response(status=status.HTTP_200_OK)


class DeleteUserAPI(DestroyAPIView):
    ''' Delete User '''
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
