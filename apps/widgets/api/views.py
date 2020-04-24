from rest_framework import generics
from widgets.models import Widget
from widgets.api.serializers import WidgetSerializer


class WidgetListAPIView(generics.ListCreateAPIView):
    serializer_class = WidgetSerializer
    queryset = Widget.objects.all()


class WidgetAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WidgetSerializer
    queryset = Widget.objects.all()
    # permission_classes = []
    # lookup_url_kwarg = 'id'
    # lookup_field = 'id'
