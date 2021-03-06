from django.db import models
from django.conf import settings
import uuid

from audio_src.apps.metas.models import Meta


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, default='')
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField(blank=True)
    ping = models.BooleanField(default=True)
    status = models.CharField(max_length=30, default='publish')
    isDeleted = models.BooleanField(default=False)
    # RelationShip
    meta = models.OneToOneField(Meta, on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.SET_NULL, null=True, unique=True)
    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.id)
