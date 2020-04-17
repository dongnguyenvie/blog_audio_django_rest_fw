from django.db import models


class Setting(models.Model):
    key = models.CharField(max_length=30, default='')
    value = models.TextField()
    option = models.TextField()
    isDelete = models.BooleanField(default=False)
    default = models.TextField(default='')
