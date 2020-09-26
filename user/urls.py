"""User URL Configuration"""

from django.urls import path
from user.views import (GetUserAPI,
                        CreateUserAPI,
                        LoginUserAPI,
                        LogoutUserAPI,
                        UpdateUserAPI,
                        UploadUserPicAPI,
                        FollowUserAPI,
                        DeleteUserAPI)

urlpatterns = [

    path('login/',
         LoginUserAPI.as_view(),
         name='login_user_api'),

    path('logout/<int:pk>/',
         LogoutUserAPI.as_view(),
         name='logout_user_api'),

    path('create/',
         CreateUserAPI.as_view(),
         name='create_user_api'),

    path('get/<int:pk>/',
         GetUserAPI.as_view(),
         name='get_user_api'),

    path('update/<int:pk>/',
         UpdateUserAPI.as_view(),
         name='update_user_api'),

    path('upload/<int:pk>/',
         UploadUserPicAPI.as_view(),
         name='upload_user_pic_api'),

    path('follow/<int:req_user_pk>/<int:ig_user_pk>/',
         FollowUserAPI.as_view(),
         name='follow_user-api'),

    path('delete/<int:pk>/',
         DeleteUserAPI.as_view(),
         name='delete_user_api'),

]
