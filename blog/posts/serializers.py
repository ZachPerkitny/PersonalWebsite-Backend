from rest_framework import serializers
from .models import Comment, Post, Tag


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'author', 'content', 'created',)


class TagListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    tags = TagListSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'summary', 'created', 'slug',  'tags',)


class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    tags = TagListSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'content', 'summary', 'created', 'slug', 'tags', 'comments',)
