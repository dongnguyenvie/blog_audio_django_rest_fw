from rest_framework import generics, pagination, response, views, filters, viewsets
from audio_src.apps.articles.models import Article
from audio_src.apps.metas.models import Meta
from audio_src.apps.articles.api.serializers import PostSerializer
from django.http import JsonResponse
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend, filterset
import django_filters
from django.db import models
from audio_src.apps.utils.filters.extends import RelatedOrderingFilter


class ArticleFilter(django_filters.rest_framework.FilterSet):
    view = django_filters.CharFilter(
        field_name='meta__view', lookup_expr='contains')
    view__gt = django_filters.CharFilter(
        field_name='meta__view', lookup_expr='gt')
    view__gte = django_filters.CharFilter(
        field_name='meta__view', lookup_expr='gte')
    view__lt = django_filters.CharFilter(
        field_name='meta__view', lookup_expr='lt')
    view__lte = django_filters.CharFilter(
        field_name='meta__view', lookup_expr='lte')
    title = django_filters.CharFilter(lookup_expr='contains')
    content = django_filters.CharFilter(lookup_expr='contains')
    timestamp__gt = django_filters.CharFilter(lookup_expr='gt')
    timestamp__gte = django_filters.CharFilter(lookup_expr='gte')
    timestamp__lt = django_filters.CharFilter(lookup_expr='lt')
    timestamp__lte = django_filters.CharFilter(lookup_expr='lte')

    class Meta:
        model = Article
        fields = ['view', 'view__gt', 'view__gte', 'view__lt', 'view__lte', 'title',
                  'content', 'timestamp__gt', 'timestamp__gte', 'timestamp__lt', 'timestamp__lte']


class ArticleListView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Article.objects.all()

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, RelatedOrderingFilter]
    filter_class = ArticleFilter
    filterset_fields = '__all__'
    ordering_fields = ('__all_related__')
    # def get_queryset(self):
    #     queryset = None
    #     pk = self.request.query_params.get('pk', None)
    #     pks = self.request.query_params.get('pks', None)
    #     if pk is not None:
    #         queryset = Article.objects.get(pk=pk)
    #         return response.Response(queryset)
    #     elif pks is not None:
    #         pks = [int(x) for x in pks.split(',')]
    #         queryset = Article.objects.filter(pk__in=pks)
    #     else:
    #         queryset = super(PostListAPIView, self).get_queryset()
    #     return queryset


class ArticleDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Article.objects.all()
    # permission_classes = []
    # lookup_url_kwarg = 'id'
    # lookup_field = 'id'


class ArticleDetailBySlugView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Article.objects.all()
    lookup_field = 'slug'
