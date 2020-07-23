from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from audio_src.apps.blogs.models import Blog
from audio_src.apps.blogs.api.serializers import BlogSerializer

class BlogListAPIView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    ordering = ('-timestamp')
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    ordering_fields = ('__all__')

class BlogAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    # permission_classes = []
    # lookup_url_kwarg = 'id'
    # lookup_field = 'id'