from django.urls import path

from comment.views import CreateCommentAPI, DeleteCommentAPI

urlpatterns = [

    path('create/<int:post_pk>/<int:req_user_pk>/',
         CreateCommentAPI.as_view(),
         name='login_user_api'),

    path('delete/<int:pk>/',
         DeleteCommentAPI.as_view(),
         name='logout_user_api'),

]
