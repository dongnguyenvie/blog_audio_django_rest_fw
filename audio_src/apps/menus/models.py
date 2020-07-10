import json
from django.db import models
from audio_src.apps.metas.models import Meta
import audio_src.apps.commons_app.constans as constans
import uuid

class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, default='')
    html = models.TextField(default=json.dumps({}))
    status = models.CharField(max_length=30, default='publish')
    isDelete = models.BooleanField(default=False)
    type = models.IntegerField(choices=constans.menu['TYPE_OPTIONS'])
    # RelationShip
    # meta = models.OneToOneField(Meta, on_delete=models.CASCADE, null=True)
    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
