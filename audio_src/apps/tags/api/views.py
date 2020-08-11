from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from audio_src.apps.utils import constants
from audio_src.apps.tags.api.serializers import TagSerializers
from audio_src.apps.tags.models import Tag


class TagListView(generics.ListCreateAPIView):
    serializer_class = TagSerializers
    queryset = Tag.objects.all()
    ordering = ('-timestamp')

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    ordering_fields = ('__all__')

    @method_decorator(cache_page(constants.CACHE_TIME_TTL), name="tags")
    def list(self, *args, **kwargs):
        return super(TagListView, self).list(self, *args, **kwargs)


class TagDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializers
    queryset = Tag.objects.all()


class TagDetailsWithSlugView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializers
    queryset = Tag.objects.all()
    lookup_field = 'slug'
