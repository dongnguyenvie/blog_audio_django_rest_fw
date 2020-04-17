from django.db import models
from metas.models import Meta

class Menu(models.Model):
    name = models.CharField(max_length=50, default='')
    html = models.TextField()
    status = models.CharField(max_length=30, default='publish')
    isDelete = models.BooleanField(default=False)
    # RelationShip
    meta = models.OneToOneField(Meta, on_delete=models.CASCADE, null=True)
    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
