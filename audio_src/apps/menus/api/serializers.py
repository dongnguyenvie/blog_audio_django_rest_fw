from rest_framework import serializers
from audio_src.apps.metas.api.serializers import MetaSerializers
from audio_src.apps.menus.models import Menu


class MenuSerializers(serializers.ModelSerializer):
    # meta = MetaSerializers()

    class Meta:
        model = Menu
        fields = '__all__'
