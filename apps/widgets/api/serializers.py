from rest_framework import serializers
from widgets.models import Widget
from metas.api.serializers import MetaSerializers


class WidgetSerializer(serializers.ModelSerializer):
    meta = MetaSerializers()

    class Meta:
        model = Widget
        fields = '__all__'
