from django.db import models
import uuid


class Settings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    key = models.CharField(max_length=30)
    value = models.TextField(blank=True, null=True)
    option = models.TextField(blank=True, null=True)
    isDeleted = models.BooleanField(default=False)
    default = models.TextField(default='')
