from django.db import models
from metas.models import Meta


class Tag(models.Model):
    title: models.TextField()
    content: models.TextField()
    isDelete: models.BooleanField(default=False)
    # ReplationShip
    meta = models.OneToOneField(Meta, on_delete=models.CASCADE)
    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
