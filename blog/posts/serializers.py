from rest_framework import serializers
from .models import Comment, Post


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'author', 'content', 'created',)


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'summary', 'created', 'slug', )


class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'content', 'summary', 'created', 'slug', 'comments',)
