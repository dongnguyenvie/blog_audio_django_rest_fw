from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from audio_src.apps.users.models import CustomUser
from audio_src.apps.users.api.serializers import UserSerializer
from audio_src.apps.users.api import serializers
from audio_src.apps.utils.permissions.Permissions import IsUserPermissionsView

class UserListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsUserPermissionsView]

    def post(self, request, *args, **kwargs):
        owner = request.user or None
        if not owner and owner.is_superuser and owner.is_staff:
            return self.create(request, *args, **kwargs)

        request.data['is_superuser'] = False
        request.data['is_staff'] = False
        return self.create(request, *args, **kwargs)

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
