from rest_framework import generics
from audio_src.apps.tags.api.serializers import TagSerializers
from audio_src.apps.tags.models import Tag


class TagListAPIView(generics.ListCreateAPIView):
    serializer_class = TagSerializers
    queryset = Tag.objects.all()


class TagAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializers
    queryset = Tag.objects.all()
