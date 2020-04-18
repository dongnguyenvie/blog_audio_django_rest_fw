from rest_framework import generics
from setting.api.serializers import SettingSerializer
from setting.models import Setting


class SettingListAPIView(generics.ListCreateAPIView):
    serializer_class = SettingSerializer
    queryset = Setting.objects.all()
