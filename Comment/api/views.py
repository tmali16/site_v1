from django.db.models import *
from rest_framework.filters import OrderingFilter, SearchFilter

from rest_framework.generics import *

from Comment.api.serializer import CommentSerializer
from ..models import Comment


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.filter(object_id=2).all()
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content', 'user__first_name']

    # def get_queryset(self, *args, **kwargs):
    #     queryset_list = Comment.objects.filter(object_id=1).all()
    #     query = self.request.GET.get("q")
    #     if query:
    #         queryset_list = queryset_list.filter(
    #             Q(content__icontains=query) |
    #             Q(user_first_name__icontains=query) |
    #             Q(user_last_name_icontains=query)
    #         ).distinc()
    #     return queryset_list
