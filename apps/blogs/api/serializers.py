from rest_framework import serializers
from blogs.models import Blog
from metas.api.serializers import MetaSerializers


class BlogSerializer(serializers.ModelSerializer):
    meta = MetaSerializers()
    class Meta:
        model = Blog
        fields = '__all__'
