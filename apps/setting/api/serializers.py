from rest_framework import serializers
from setting.models import Setting


class SettingSerializer(serializers.Serializer):
    class Meta:
        model = Setting
        fields = '__all__'
