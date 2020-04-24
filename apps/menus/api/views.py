from rest_framework import generics
from menus.api.serializers import MenuSerializers
from menus.models import Menu


class MenuListAPIView(generics.ListCreateAPIView):
    serializer_class = MenuSerializers
    queryset = Menu.objects.all()


class MenuAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializers
    queryset = Menu.objects.all()
