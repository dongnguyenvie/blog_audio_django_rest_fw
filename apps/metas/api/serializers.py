from rest_framework import serializers
from metas.models import Meta as MetaModel


class MetaSerializers(serializers.ModelSerializer):
    class Meta:
        model = MetaModel
        fields = '__all__'
