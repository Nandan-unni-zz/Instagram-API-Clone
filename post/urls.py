from django.urls import path
from post.views import (CreatePostAPI,
                        GetPostAPI,
                        UpdatePostAPI,
                        DeletePostAPI,
                        LikePostAPI,
                        SavePostAPI)

urlpatterns = [

    path('post/create/',
         CreatePostAPI,
         name='create_post_api'),

    path('post/get/<int:pk>/',
         GetPostAPI,
         name='create_post_api'),

    path('post/update/<int:pk>/',
         UpdatePostAPI,
         name='create_post_api'),

    path('post/delete/<int:pk>/',
         DeletePostAPI,
         name='create_post_api'),

    path('post/like/<int:req_user_pk>/<int:post_pk>/',
         LikePostAPI,
         name='create_post_api'),

    path('post/save/<int:req_user_pk>/<int:post_pk>/',
         SavePostAPI,
         name='create_post_api'),

]
