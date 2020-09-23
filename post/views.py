from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from post.serializers import CreatePostSerializer, PostSerializer
from post.models import Post

class CreatePostAPI(CreateAPIView):
    serializer_class = CreatePostSerializer
    queryset = Post.objects.all()


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
        pass


class SavePostAPI(APIView):
    def get(self, request, *args, **kwargs):
        pass

