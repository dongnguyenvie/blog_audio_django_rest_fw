from rest_framework import serializers
from audio_src.apps.metas.models import Meta as MetaModel


class MetaSerializers(serializers.ModelSerializer):
    class Meta:
        model = MetaModel
        fields = '__all__'
