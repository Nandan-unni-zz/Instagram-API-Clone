""" User API views for CRUD and other operations """

# Views and Responses
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView

# Sending Mails
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

# Django Tools
from django.contrib.auth import get_user_model, authenticate, login, logout

# Local Imports
from user.serializers import CreateUserSerializer, UserSerializer, UploadUserPicSerializer
from user.tests import message


class LoginUserAPI(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_deactivated:
                return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                                data={'error': 'This account is deactivated.'})
            login(request, user)
            message(user.username + ' logged in.')
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                        data={'error': 'Invalid credentials'})


class LogoutUserAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            user = get_user_model().objects.get(pk=kwargs['pk'])
        except get_user_model().DoesNotExist:
            user = None
            message('User not found.')
        if user is not None:
            message(user.username + ' logged out.')
            logout(user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'User not found.'})


class CreateUserAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.full_name = user.full_name.title()
            user.is_active = True
            user.save()
            message(user.username + ' created an account.')
            code = 309756
            email_subject = '{} is your Instagram Code'.format(code)
            mail = render_to_string('activate_mail.html', {'email': user.email, 'code': code})
            to_email = user.email
            email = EmailMessage(email_subject, mail, from_email='Instagram', to=[to_email])
            email.content_subtype = 'html'
            email.send()
            message('Email send to ' + user.username)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, data=serializer.errors)


class GetUserAPI(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class UpdateUserAPI(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class UploadUserPicAPI(UpdateAPIView):
    serializer_class = UploadUserPicSerializer
    queryset = get_user_model().objects.all()


class FollowUserAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            req_user = get_user_model().objects.get(pk=kwargs['req_user_pk'])
        except get_user_model().DoesNotExist:
            req_user = None
            message('User not found.')
        try:
            ig_user = get_user_model().objects.get(pk=kwargs['ig_user_pk'])
        except get_user_model().DoesNotExist:
            ig_user = None
            message('User not found')
        if req_user is not None and ig_user is not None:
            if req_user in ig_user.followers.all():
                ig_user.followers.remove(req_user)
                req_user.following.remove(ig_user)
                message(req_user.username + ' unfollowed ' + ig_user.username)
            else:
                ig_user.followers.add(req_user)
                req_user.following.add(ig_user)
                message(req_user.username + ' followed ' + ig_user.username)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class DeleteUserAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            username = get_user_model().objects.get(pk=kwargs['pk']).username
        except get_user_model().DoesNotExist:
            username = None
        if username is not None:
            password = request.data.get('password', None)
            user = authenticate(username=username, password=password)
            if user is not None:
                message(user.username + ' deleted their account.')
                user.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                            data={'error': 'Invalid credentials'})
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                        data={"error": "Invalid credentials"})


class DeactivateUserAPI(APIView):
    def post(self, request, *args, **kwargs):
        username = get_user_model().objects.get(pk=kwargs['pk']).username
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            message(user.username + ' deactivated their account.')
            user.is_deactivated = True
            user.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                        data={'error': 'Invalid credentials'})


class GetProfileAPI(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = None
