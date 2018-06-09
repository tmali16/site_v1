from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from Comment.models import Comment


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'content_type',
            'object_id',
            'parent',
            'username',
            'content'
        ]
