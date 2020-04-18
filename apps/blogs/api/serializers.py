from rest_framework import serializers
from blogs.models import Blog
from metas.api.serializers import MetaSerializers


class BlogSerializer(serializers.ModelSerializer):
    meta = MetaSerializers()
    # more_filed = serializers.SerializerMethodField()
    # hahaha = serializers.CharField(
    #     required=False, default='some_default_value')

    class Meta:
        model = Blog
        fields = '__all__'

    def create(self, validated_data):
        meta_data = validated_data.pop('meta')
        meta = MetaSerializers.create(
            MetaSerializers(), validated_data=meta_data)
        validated_data['meta'] = meta
        blog, created = Blog.objects.update_or_create(**validated_data)
        return blog

    # def get_more_filed(self, obj):
    #     return "1aaaaa"
