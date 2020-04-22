from queue import Queue
from rest_framework import serializers, response, status
from posts.models import Post
# from tags.models import Tag
from metas.api.serializers import MetaSerializers, MetaModel
from commons.crawler.spider import Spider
from commons.Validator.post_validator import get_blog_and_owner_validator
# from categories.api.serializers import CategorySerializers

q = Queue()
# Init threading
Spider(q)


class PostSerializer(serializers.ModelSerializer):
    meta = MetaSerializers(required=False)
    id_audio = serializers.CharField(
        required=False, default='')
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    blog = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        [owner, blog] = get_blog_and_owner_validator(self, validated_data)

        id_audio = validated_data.pop('id_audio', None)
        tags_data = validated_data.pop('tags', [])
        categories_data = validated_data.pop('categories', [])
        meta_data = validated_data.pop('meta', None)
        meta_serializer = self.fields['meta']

        if meta_data:
            meta = meta_serializer.create(validated_data=meta_data)
            validated_data['meta'] = meta

        validated_data['blog'] = blog
        post_created = Post.objects.create(**validated_data)

        if categories_data or tags_data:
            for category_id in categories_data:
                post_created.categories.add(category_id)
            for tag_id in tags_data:
                post_created.categories.add(tag_id)
            post_created.save()

        if id_audio:
            # Crawl threading
            validated_data['source'] = "processing"
            Spider.create_archive_crawl_jobs(post_created, id_audio)

        return post_created

    def update(self, instance, validated_data):
        [owner, blog] = get_blog_and_owner_validator(self, validated_data)

        id_audio = validated_data.pop('id_audio', None)
        meta_data = validated_data.pop('meta', None)
        meta_instance = instance.meta
        meta_serializer = self.fields['meta']

        post_updated = super().update(instance, validated_data)

        if meta_data:
            meta = meta_serializer.update(
                instance=meta_instance, validated_data=meta_data)
            post_updated.meta = meta
         # Crawl threading
        if id_audio:
            post_updated.source = 'processing'
            Spider.create_archive_crawl_jobs(post_updated, id_audio)
        return post_updated
