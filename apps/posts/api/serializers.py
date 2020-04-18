from rest_framework import serializers
from posts.models import Post
from metas.api.serializers import MetaSerializers


class PostSerializer(serializers.ModelSerializer):
    meta = MetaSerializers()

    class Meta:
        model = Post
        fields = '__all__'
