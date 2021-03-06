from django.db import models
import uuid

from audio_src.apps.metas.models import Meta


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(max_length=30, default='')
    slug = models.SlugField(unique=True)
    # slug = models.SlugField(null=True, blank=True)
    content = models.TextField(default='', null=True, blank=True)
    isDeleted = models.BooleanField(default=False)
    # ReplationShip
    meta = models.OneToOneField(
        Meta, on_delete=models.SET_NULL, null=True, blank=True)
    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    # def __str__(self):
    #     return self.title
