from django.db import models
from blogs.models import Blog
from customers.models import Customer
from tags.models import Tag
from categories.models import Category
from metas.models import Meta


class Post(models.Model):
    title = models.CharField(max_length=50, default='')
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(default='')
    content = models.TextField(default='')
    source = models.TextField(blank=True)
    ping = models.BooleanField(default=True)
    type = models.CharField(max_length=30, default='post')
    status = models.CharField(max_length=30, default='publish')
    # RelationShip
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    meta = models.OneToOneField(Meta, on_delete=models.CASCADE, null=True)
    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

# class Post(models.Model):
#     content = models.TextField()
#     slug = models.SlugField(unique=True)
#     updated = models.DateTimeField(auto_now=True, auto_now_add=False)
#     timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

#     def __str__(self):
#         return self.content

#     class Meta:
#         ordering = ["timestamp", "updated"]
