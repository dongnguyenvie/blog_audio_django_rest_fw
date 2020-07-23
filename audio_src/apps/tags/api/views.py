from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from audio_src.apps.tags.api.serializers import TagSerializers
from audio_src.apps.tags.models import Tag


class TagListAPIView(generics.ListCreateAPIView):
    serializer_class = TagSerializers
    queryset = Tag.objects.all()
    ordering = ('-timestamp')

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    ordering_fields = ('__all__')

class TagAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializers
    queryset = Tag.objects.all()
