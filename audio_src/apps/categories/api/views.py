from rest_framework import generics, filters
from audio_src.apps.categories.models import Category
from audio_src.apps.categories.api.serializers import CategorySerializers
from django_filters.rest_framework import DjangoFilterBackend


class CategoryListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    ordering = ('-timestamp')

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    ordering_fields = ('__all__')


class CategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
