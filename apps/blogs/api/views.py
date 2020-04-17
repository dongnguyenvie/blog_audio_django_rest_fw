from rest_framework import generics
from blogs.models import Blog
from blogs.api.serializers import BlogSerializer


class BlogListAPIView(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
