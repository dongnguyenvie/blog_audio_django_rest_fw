from rest_framework import serializers
from categories.models import Category
from metas.api.serializers import MetaSerializers


class CategorySerializers(serializers.ModelSerializer):
    meta = MetaSerializers()

    class Meta:
        model = Category
        fields = '__all__'
