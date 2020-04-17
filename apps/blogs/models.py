from django.db import models
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50, default='')
    slug = models.SlugField(unique=True)
    excerpt = models.TextField()
    content = models.TextField()
    ping = models.BooleanField(default=True)
    status = models.CharField(max_length=30, default='publish')
    # RelationShip

    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
