from rest_framework import generics
from posts.models import Post
from posts.api.serializers import PostSerializer


class PostListAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
# PostListAPIView.
