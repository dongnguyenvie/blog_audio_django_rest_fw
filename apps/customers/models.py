from django.db import models
from django.contrib.auth.models import User
from blogs.models import Blog
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.URLField(null=True, blank=True)
