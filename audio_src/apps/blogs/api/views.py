from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from audio_src.apps.blogs.models import Blog
from audio_src.apps.blogs.api.serializers import BlogSerializer
from audio_src.apps.utils import constants


class BlogListListView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    ordering = ('-timestamp')
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    ordering_fields = ('__all__')

    @method_decorator(cache_page(constants.CACHE_TIME_TTL), name="articles")
    def list(self, *args, **kwargs):
        return super(BlogListListView, self).list(self, *args, **kwargs)


class BlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    # permission_classes = []
    # lookup_url_kwarg = 'id'
    # lookup_field = 'id'
