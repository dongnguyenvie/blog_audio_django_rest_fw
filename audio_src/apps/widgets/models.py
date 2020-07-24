from django.db import models
import uuid

from audio_src.apps.metas.models import Meta


class Widget(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=30, default='none')
    title = models.CharField(max_length=30, default='')
    isDeleted = models.BooleanField(default=False)
    image = models.URLField(blank=True)
    url = models.URLField(blank=True)
    size = models.CharField(max_length=30)
    # RelationShip
    meta = models.OneToOneField(Meta, on_delete=models.SET_NULL, null=True)
    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
