"""User URL Configuration"""

from django.urls import path
from user.views import (GetUserAPI,
                        CreateUserAPI,
                        UpdateUserAPI,
                        FollowUserAPI,
                        DeleteUserAPI)

urlpatterns = [

    path('create/',
         CreateUserAPI.as_view(),
         name='create_user_api'),

    path('get/<int:pk>/',
         GetUserAPI.as_view(),
         name='get_user_api'),

    path('update/<int:pk>/',
         UpdateUserAPI.as_view(),
         name='update_user_api'),

    path('follow/<int:pk>/',
         FollowUserAPI.as_view(),
         name='follow_user-api'),

    path('delete/<int:pk>/',
         DeleteUserAPI.as_view(),
         name='delete_user_api'),

]
