from django.db import models

# Create your models here.


class Meta(models.Model):
    jsonLd = models.TextField()
    view = models.BigIntegerField(default=0)
    like = models.BigIntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.id)
