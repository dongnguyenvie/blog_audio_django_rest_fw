from rest_framework import serializers
from metas.api.serializers import MetaSerializers
from menus.models import Menu


class MenuSerializers(serializers.ModelSerializer):
    # meta = MetaSerializers()

    class Meta:
        model = Menu
        fields = '__all__'
