from django.db import models
import uuid
from audio_src.apps.utils import constants


class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=True, null=True)
    data = models.CharField(max_length=200)
    path = models.CharField(max_length=300, null=True)
    type = models.IntegerField(
        choices=constants.media_type['TYPE_OPTIONS'], default=1)
    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
