from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from Posts.models import Post


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = []
