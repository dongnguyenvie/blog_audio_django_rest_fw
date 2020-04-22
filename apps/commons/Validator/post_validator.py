from rest_framework.serializers import ValidationError


def get_blog_and_owner_validator(self, validated_data):
    owner = validated_data.pop('owner', None)
    blog = None if not owner else owner.customer.blog
    if not blog:
        raise ValidationError({"message": "blog not exists"})
    return [owner, blog]
    # if not validated_data['tags'] or 'tags' not in validated_data:
    #     validated_data.pop('tags')
    # if not validated_data['categories'] or 'categories' not in validated_data:
    #     validated_data.pop('categories')
