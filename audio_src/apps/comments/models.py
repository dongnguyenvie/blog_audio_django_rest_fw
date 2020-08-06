import uuid
from django.db import models
from audio_src.apps.articles.models import Article


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    parrentId = models.UUIDField(null=True, blank=True)
    isDeleted = models.BooleanField(default=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    user = models.TextField(default='', blank=True, null=True)
    view = models.BigIntegerField(default=0)
    like = models.BigIntegerField(default=0)
    content = models.TextField(default='', blank=True, null=True)
    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
