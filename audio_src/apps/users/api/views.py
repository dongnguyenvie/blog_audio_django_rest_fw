from rest_framework import generics, permissions
from audio_src.apps.users.models import CustomUser
from audio_src.apps.users.api.serializers import UserSerializer


class UserListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = []


class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
