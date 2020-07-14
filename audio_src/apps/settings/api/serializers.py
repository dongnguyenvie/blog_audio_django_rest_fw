from rest_framework import serializers
from audio_src.apps.settings.models import Settings


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'
