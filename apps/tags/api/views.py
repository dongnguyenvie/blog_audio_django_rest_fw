from rest_framework import generics
from tags.api.serializers import TagSerializers
from tags.models import Tag


class TagListAPIView(generics.ListCreateAPIView):
    serializer_class = TagSerializers
    queryset = Tag.objects.all()


class TagAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializers
    queryset = Tag.objects.all()
