from queue import Queue
from rest_framework import serializers
from posts.models import Post
# from tags.models import Tag
from metas.api.serializers import MetaSerializers
from commons.crawler.spider import Spider

q = Queue()
# Init threading
Spider(q)


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
        if not validated_data['tags'] or 'tags' not in validated_data:
            validated_data.pop('tags')
        if not validated_data['categories'] or 'categories' not in validated_data:
            validated_data.pop('categories')

        id_audio = validated_data.pop('id_audio')
        meta_data = validated_data.pop('meta')

        meta = MetaSerializers.create(
            MetaSerializers(), validated_data=meta_data)

        validated_data['source'] = "processing"
        validated_data['meta'] = meta

        post_created = Post.objects.create(**validated_data)
        # Crawl threading
        Spider.create_archive_crawl_jobs(post_created, id_audio)
        return post_created
