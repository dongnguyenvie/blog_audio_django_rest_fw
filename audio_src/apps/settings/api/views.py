from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from audio_src.apps.utils import constants
from audio_src.apps.settings.api.serializers import SettingSerializer
from audio_src.apps.settings.models import Settings


class SettingTableResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class SettingListView(generics.ListCreateAPIView):
    serializer_class = SettingSerializer
    queryset = Settings.objects.all()
    pagination_class = None

    @method_decorator(cache_page(constants.CACHE_TIME), name="articles")
    def list(self, *args, **kwargs):
        return super(ArticleListView, self).list(self, *args, **kwargs)


class SettingDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SettingSerializer
    queryset = Settings.objects.all()
