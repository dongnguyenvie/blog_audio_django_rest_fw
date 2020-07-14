from rest_framework import generics
from audio_src.apps.categories.models import Category
from audio_src.apps.categories.api.serializers import CategorySerializers


class CategoryListAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()

class CategoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    # permission_classes = []
    # lookup_url_kwarg = 'id'
    # lookup_field = 'id'
