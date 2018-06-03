from rest_framework.generics import *

from Posts.api.serializer import PostSerializer, ServiceSerializer
from ..models import Post
from Service.models import Service


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetaileViewAPI(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
