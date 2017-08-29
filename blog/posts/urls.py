from django.conf.urls import url
from .views import PostDetailView, PostListView, CommentsCreateView

urlpatterns = [
    url(r'^$', PostListView.as_view()),
    url(r'^(?P<slug>[-_\w]+)/$', PostDetailView.as_view()),
    url(r'^(?P<slug>[-_\w]+)/comments/$', CommentsCreateView.as_view())
]
