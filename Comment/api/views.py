from rest_framework.generics import *

from Comment.api.serializer import CommentSerializer
from ..models import Comment


class CommentAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
