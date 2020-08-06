from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend

from audio_src.apps.utils import constants
from audio_src.apps.comments.api.serializers import CommentSerializer
from audio_src.apps.comments.models import Comment


class SettingTableResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    pagination_class = None
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    @method_decorator(cache_page(constants.CACHE_TIME_TTL), name="comments")
    def list(self, *args, **kwargs):
        return super(CommentListView, self).list(self, *args, **kwargs)


class CommentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
