from rest_framework.serializers import ValidationError
from rest_framework import status, permissions
from audio_src.apps.utils.validator.extends import BlogValidationError, OwnerNotExistsValidationError


def getOwnerAndBlog(self, validated_data):
    owner = validated_data.pop('owner', None)
    blog = None if not owner else owner.blog
    if not blog:
        raise BlogValidationError()
    return [owner, blog]


def getOwner(self, validated_data):
    owner = validated_data.pop('owner', None)
    if not owner:
        raise OwnerNotExistsValidationError()
    return owner
