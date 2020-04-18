from rest_framework import generics
from advises.models import Advise
from advises.api.serializers import AdviseSerializer


class AdviseListAPIView(generics.ListCreateAPIView):
    serializer_class = AdviseSerializer
    queryset = Advise.objects.all()
