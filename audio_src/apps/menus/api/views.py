from rest_framework import generics
from audio_src.apps.menus.api.serializers import MenuSerializers
from audio_src.apps.menus.models import Menu


class MenuListView(generics.ListCreateAPIView):
    serializer_class = MenuSerializers
    queryset = Menu.objects.all()


class MenuDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializers
    queryset = Menu.objects.all()
