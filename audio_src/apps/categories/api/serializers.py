from rest_framework import serializers
from audio_src.apps.categories.models import Category
from audio_src.apps.metas.api.serializers import MetaSerializers
from audio_src.apps.utils.serializers.helper import get_owner_and_blog
from drf_queryfields import QueryFieldsMixin


class CategorySerializers(QueryFieldsMixin, serializers.ModelSerializer):
    meta = MetaSerializers(required=False)
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        [owner, blog] = get_owner_and_blog(self, validated_data)
        meta_data = validated_data.pop("meta", {})
        meta_serializer = self.fields['meta']

        meta = meta_serializer.create(validated_data=meta_data)

        validated_data['meta'] = meta

        category_created = Category.objects.create(**validated_data)
        return category_created

    def update(self, instance, validated_data):
        [owner, blog] = get_owner_and_blog(self, validated_data)

        meta_data = validated_data.pop('meta', None)
        meta_instance = instance.meta
        meta_serializer = self.fields['meta']

        category_created = super().update(instance, validated_data)

        if meta_data:
            meta = meta_serializer.update(
                instance=meta_instance, validated_data=meta_data)
            category_created.meta = meta

        return category_created
