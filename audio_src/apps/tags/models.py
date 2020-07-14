from django.db import models
from audio_src.apps.metas.models import Meta
import uuid

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(max_length=30, default='')
    content = models.TextField(default='')
    isDeleted = models.BooleanField(default=False)
    # ReplationShip
    meta = models.OneToOneField(Meta, on_delete=models.CASCADE)
    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
