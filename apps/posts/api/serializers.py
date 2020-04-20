from queue import Queue
from rest_framework import serializers
from posts.models import Post
# from tags.models import Tag
from metas.api.serializers import MetaSerializers, MetaModel
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

    def update(self, instance, validated_data):
        id_audio = validated_data.pop('id_audio', None)
        meta_data = validated_data.pop('meta')
        meta_pk = None

        post_updated = super().update(instance, validated_data)

        try:
            meta_pk = instance.meta.id
        except KeyError:
            pass

        if meta_pk:
            meta_instance = MetaModel.objects.get(pk=meta_pk)
            meta = MetaSerializers.update(MetaSerializers(), instance=meta_instance,
                                          validated_data=meta_data)
            post_updated.meta = meta
        if id_audio:
            post_updated.source = 'processing'
            Spider.create_archive_crawl_jobs(post_updated, id_audio)
        return post_updated
