from rest_framework import generics
from setting.api.serializers import SettingSerializer
from setting.models import Setting
from rest_framework.pagination import PageNumberPagination


class SettingTableResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class SettingListAPIView(generics.ListCreateAPIView):
    serializer_class = SettingSerializer
    queryset = Setting.objects.all()
    pagination_class = SettingTableResultsSetPagination
