from rest_framework import serializers
from audio_src.apps.metas.api.serializers import MetaSerializers
from audio_src.apps.tags.models import Tag


class TagSerializers(serializers.ModelSerializer):
    # meta = MetaSerializers()

    class Meta:
        model = Tag
        fields = '__all__'
