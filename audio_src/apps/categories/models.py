from django.db import models
from audio_src.apps.metas.models import Meta


class Category(models.Model):
    title = models.CharField(max_length=50, default='')
    description = models.TextField(default='')
    status = models.CharField(max_length=30, default='publish')
    # ReplationShip
    meta = models.OneToOneField(Meta, on_delete=models.CASCADE)
    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
