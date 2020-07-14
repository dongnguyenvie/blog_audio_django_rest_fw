from rest_framework import serializers
from audio_src.apps.widgets.models import Widget
from audio_src.apps.metas.api.serializers import MetaSerializers


class WidgetSerializer(serializers.ModelSerializer):
    meta = MetaSerializers()

    class Meta:
        model = Widget
        fields = '__all__'
