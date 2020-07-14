from django.db import models
from django.contrib.auth.models import User
from audio_src.apps.blogs.models import Blog
from audio_src.apps.metas.models import Meta
import uuid

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # RelationShip
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blog = models.OneToOneField(
        Blog, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.URLField(null=True, blank=True)
    meta = models.OneToOneField(Meta, on_delete=models.CASCADE, null=True, blank=True)
    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.id)
