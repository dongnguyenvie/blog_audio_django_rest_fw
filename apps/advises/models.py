from django.db import models
from metas.models import Meta


class Advise(models.Model):
    type = models.CharField(max_length=30, default='none')
    title = models.CharField(max_length=30, default='')
    isDelete = models.BooleanField(default=False)
    image = models.URLField(blank=True)
    url = models.URLField(blank=True)
    size = models.CharField(max_length=30)
    # RelationShip
    meta = models.OneToOneField(Meta, on_delete=models.CASCADE, null=True)
    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
