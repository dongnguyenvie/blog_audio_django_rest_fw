from django_filters.rest_framework import filterset
import django_filters
from audio_src.apps.articles.models import Article

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
