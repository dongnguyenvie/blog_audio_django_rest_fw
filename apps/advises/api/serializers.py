from rest_framework import serializers
from advises.models import Advise
from metas.api.serializers import MetaSerializers


class AdviseSerializer(serializers.ModelSerializer):
    meta = MetaSerializers()

    class Meta:
        model = Advise
        fields = '__all__'
