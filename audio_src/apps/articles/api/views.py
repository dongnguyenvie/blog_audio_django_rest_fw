from rest_framework import generics, views, filters
from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from audio_src.apps.utils import constants
from audio_src.apps.articles.models import Article
from audio_src.apps.articles.api.serializers import ArticleSerializer
from audio_src.apps.utils.filters.extends import RelatedOrderingFilter
from audio_src.apps.articles.filters import ArticleFilter


class ArticleListView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    ordering = ('?')

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, RelatedOrderingFilter]
    filter_class = ArticleFilter
    filterset_fields = '__all__'
    ordering_fields = ('__all_related__')

    # @method_decorator(cache_page(constants.CACHE_TIME_TTL), name="articles")
    def list(self, *args, **kwargs):
        return super(ArticleListView, self).list(self, *args, **kwargs)


class ArticleDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'pk'


class ArticleDetailsWithSlugView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'slug'
