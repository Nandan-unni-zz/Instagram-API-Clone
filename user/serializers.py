from rest_framework import serializers
from django.contrib.auth import get_user_model

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

class UserSerializer(serializers.ModelSerializer):
    ''' Serializer for RUD operatons '''
    followers = MiniUserSerializer(many=True)
    following = MiniUserSerializer(many=True)
    class Meta:
        model = get_user_model()
        fields = ['pk', 'full_name', 'email', 'username', 'ph_number',
                  'birthday', 'profile_pic', 'website', 'bio',
                  'followers', 'followers_count',
                  'following', 'following_count']
