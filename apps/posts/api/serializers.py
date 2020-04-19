from rest_framework import serializers
import json
from posts.models import Post
from tags.models import Tag
from metas.api.serializers import MetaSerializers
from commons.crawler.spider import Spider


class PostSerializer(serializers.ModelSerializer):
    meta = MetaSerializers()
    # blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    id_audio = serializers.CharField(
        required=False, default='')

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        if not validated_data['tags']:
            validated_data.pop('tags')
        if not validated_data['categories']:
            validated_data.pop('categories')
        meta_data = validated_data.pop('meta')
        meta = MetaSerializers.create(
            MetaSerializers(), validated_data=meta_data)
        id_audio = validated_data.pop('id_audio')
        source_crawl = Spider.crawl_archive(id_audio)
        validated_data['source'] = json.dumps(source_crawl)
        validated_data['meta'] = meta
        post_created = Post.objects.create(**validated_data)
        return post_created
