from django.db import models
from django.contrib.auth.models import User
from blogs.models import Blog
from metas.models import Meta


class Customer(models.Model):
    # RelationShip
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blog = models.OneToOneField(
        Blog, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.URLField(null=True, blank=True)
    meta = models.OneToOneField(Meta, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)
