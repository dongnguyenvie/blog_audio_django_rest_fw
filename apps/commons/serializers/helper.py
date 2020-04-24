from rest_framework.serializers import ValidationError
from rest_framework import status, permissions
from ..validator.extension_validation import BlogValidationError


def get_owner_and_blog(self, validated_data):
    owner = validated_data.pop('owner', None)
    blog = None if not owner else owner.customer.blog
    if not blog:
        raise BlogValidationError()
    return [owner, blog]
