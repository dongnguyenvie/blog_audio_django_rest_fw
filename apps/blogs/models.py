from django.db import models
from metas.models import Meta


class Blog(models.Model):
    title = models.CharField(max_length=50, default='')
    slug = models.SlugField(unique=True)
    excerpt = models.TextField()
    content = models.TextField()
    ping = models.BooleanField(default=True)
    status = models.CharField(max_length=30, default='publish')
    # RelationShip
    meta = models.OneToOneField(Meta, on_delete=models.CASCADE, null=True)
    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
