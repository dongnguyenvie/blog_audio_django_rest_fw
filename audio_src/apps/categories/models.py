from django.db import models
import uuid

from audio_src.apps.metas.models import Meta


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, default='')
    slug = models.SlugField(unique=True)
    description = models.TextField(default='', null=True, blank=True)
    status = models.CharField(max_length=30, default='publish')
    isDeleted = models.BooleanField(default=False)
    # ReplationShip
    meta = models.OneToOneField(
        Meta, on_delete=models.SET_NULL, null=True, blank=True)
    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    # def __str__(self):
    #     return str(self.id)
