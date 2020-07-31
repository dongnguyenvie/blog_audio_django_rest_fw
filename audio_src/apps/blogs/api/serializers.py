from rest_framework import serializers
from audio_src.apps.blogs.models import Blog
from audio_src.apps.metas.api.serializers import MetaSerializers
from audio_src.apps.utils.serializers.helper import getOwner


class BlogSerializer(serializers.ModelSerializer):
    meta = MetaSerializers()
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Blog
        fields = '__all__'

    def create(self, validated_data):
        owner = getOwner(self, validated_data)
        # validated_data['user'] = owner.id

        meta_data = validated_data.pop('meta', {})
        meta_serializer = self.fields['meta']
        meta = meta_serializer.create(validated_data=meta_data)

        blog_created = Blog.objects.create(**validated_data)
        owner['blog'] = blog_created
        owner.save()
        return blog_created
