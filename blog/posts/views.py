from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .pagination import TotalPagesPagination
from .serializers import CommentSerializer, PostListSerializer, PostDetailSerializer


class PostListView(ListCreateAPIView):
    """
    Gets and creates blog posts.
    """

    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = TotalPagesPagination


class PostDetailByTagView(ListAPIView):
    """
    Gets all posts with some tag
    """

    serializer_class = PostListSerializer
    pagination_class = TotalPagesPagination

    def get_queryset(self):
        tag = self.kwargs['tag']
        return Post.objects.filter(tags__slug=tag)


class PostDetailView(RetrieveUpdateDestroyAPIView):
    """
    Gets, Edits and Deletes a specific post.
    """

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'slug'


class CommentsCreateView(CreateAPIView):
    """
    Allows users to post a comment
    """

    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        slug = self.kwargs['slug']
        post = get_object_or_404(Post, slug=slug)
        serializer.save(
            post=post
        )
