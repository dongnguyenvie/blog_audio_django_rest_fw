from rest_framework import serializers
from categories.models import Category
from metas.api.serializers import MetaSerializers
from commons.Validator.post_validator import get_blog_and_owner_validator


class CategorySerializers(serializers.ModelSerializer):
    meta = MetaSerializers(required=False)
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        [owner, blog] = get_blog_and_owner_validator(self, validated_data)
        meta_data = validated_data.pop("meta", {})
        meta_serializer = self.fields['meta']

        meta = meta_serializer.create(validated_data=meta_data)

        validated_data['meta'] = meta

        category_created = Category.objects.create(**validated_data)
        return category_created

    def update(self, instance, validated_data):
        [owner, blog] = get_blog_and_owner_validator(self, validated_data)

        meta_data = validated_data.pop('meta', None)
        meta_instance = instance.meta
        meta_serializer = self.fields['meta']

        category_created = super().update(instance, validated_data)

        if meta_data:
            meta = meta_serializer.update(
                instance=meta_instance, validated_data=meta_data)
            category_created.meta = meta

        return category_created
