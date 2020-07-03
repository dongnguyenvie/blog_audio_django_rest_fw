from rest_framework import generics, permissions
from audio_src.apps.customers.models import Customer
from audio_src.apps.customers.api.serializers import CustomerSerializers


class CustomerListAPIView(generics.ListCreateAPIView):
    serializer_class = CustomerSerializers
    queryset = Customer.objects.all()
    permission_classes = []


class CustomerAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializers
    queryset = Customer.objects.all()
