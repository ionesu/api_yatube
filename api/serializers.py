from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    """Class PostSerializer for Post"""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Class CommentSerializer for Comment"""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
