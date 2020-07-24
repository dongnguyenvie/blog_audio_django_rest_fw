from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from audio_src.apps.utils import constants
from audio_src.apps.categories.models import Category
from audio_src.apps.categories.api.serializers import CategorySerializers


class CategoryListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    ordering = ('-timestamp')

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    ordering_fields = ('__all__')

    @method_decorator(cache_page(constants.CACHE_TIME_TTL), name="articles")
    def list(self, *args, **kwargs):
        return super(CategoryListView, self).list(self, *args, **kwargs)


class CategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
