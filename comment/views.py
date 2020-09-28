from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, DestroyAPIView

from comment.models import Comment
from comment.serializers import CreateCommentSerializer, CommentSerializer


class CreateCommentAPI(CreateAPIView):
    serializer_class = CreateCommentSerializer
    queryset = Comment.objects.all()

class DeleteCommentAPI(DestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
