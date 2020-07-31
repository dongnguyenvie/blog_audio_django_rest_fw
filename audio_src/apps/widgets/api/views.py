from rest_framework import generics

from audio_src.apps.widgets.models import Widget
from audio_src.apps.widgets.api.serializers import WidgetSerializer


class WidgetListAPIView(generics.ListCreateAPIView):
    serializer_class = WidgetSerializer
    queryset = Widget.objects.all()


class WidgetAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WidgetSerializer
    queryset = Widget.objects.all()
    # permission_classes = []
    # lookup_url_kwarg = 'id'
    # lookup_field = 'id'
