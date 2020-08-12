from rest_framework import serializers
from audio_src.apps.blogs.models import Blog
from audio_src.apps.metas.api.serializers import MetaSerializers
from audio_src.apps.utils.serializers.helper import getOwner
from audio_src.apps.utils.validator.extends import BlogExistsError


class BlogSerializer(serializers.ModelSerializer):
    meta = MetaSerializers()
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Blog
        # fields = '__all__'
        exclude = ['isDeleted']

    def create(self, validated_data):
        owner = getOwner(self, validated_data)
        try:
            blogFound = Blog.objects.get(user=owner.id)
        except:
            blogFound = None
        if blogFound:
            raise BlogExistsError()

        validated_data['user'] = owner

        meta_data = validated_data.pop('meta', {})
        meta_serializer = self.fields['meta']
        meta = meta_serializer.create(validated_data=meta_data)

        blog_created = Blog.objects.create(**validated_data)
        return blog_created
