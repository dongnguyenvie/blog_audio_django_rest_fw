from rest_framework import serializers
from audio_src.apps.setting.models import Setting


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'
