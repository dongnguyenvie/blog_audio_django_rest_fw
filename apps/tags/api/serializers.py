from rest_framework import serializers
from metas.api.serializers import MetaSerializers
from tags.models import Tag


class TagSerializers(serializers.ModelSerializer):
    # meta = MetaSerializers()

    class Meta:
        model = Tag
        fields = '__all__'
