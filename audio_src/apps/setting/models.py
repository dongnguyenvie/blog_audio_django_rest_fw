from django.db import models
import uuid

class Setting(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    key = models.CharField(max_length=30)
    value = models.TextField()
    option = models.TextField()
    isDeleted = models.BooleanField(default=False)
    default = models.TextField(default='')
