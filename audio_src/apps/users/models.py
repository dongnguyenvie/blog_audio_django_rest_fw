import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
# from audio_src.apps.blogs.models import Blog
from audio_src.apps.metas.models import Meta


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # RelationShip
    # blog = models.OneToOneField(
    #     Blog, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.URLField(null=True, blank=True)
    meta = models.OneToOneField(
        Meta, on_delete=models.CASCADE, null=True, blank=True)
