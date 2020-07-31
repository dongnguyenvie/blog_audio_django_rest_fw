from rest_framework.serializers import ValidationError
from rest_framework import status, permissions
from audio_src.apps.utils.validator.extends import BlogValidationError, OwnerNotExistsValidationError
from audio_src.apps.blogs.models import Blog

def getOwnerAndBlog(self, validated_data):
    owner = validated_data.pop('owner', None)

    try:
        blog = Blog.objects.get(user=owner.id)
    except expression as identifier:
        raise BlogValidationError() 

    return [owner, blog]


def getOwner(self, validated_data):
    owner = validated_data.pop('owner', None)
    if not owner:
        raise OwnerNotExistsValidationError()
    return owner
