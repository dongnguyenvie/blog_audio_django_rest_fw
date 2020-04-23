from rest_framework.serializers import ValidationError
from rest_framework import status, permissions


class BlogValidationError (ValidationError):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'Blog not exits'
