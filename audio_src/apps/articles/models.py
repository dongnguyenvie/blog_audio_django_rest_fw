import uuid
from django.db import models
from audio_src.apps.blogs.models import Blog
from django.conf import settings
from django.urls import reverse

from audio_src.apps.tags.models import Tag
from audio_src.apps.categories.models import Category
from audio_src.apps.metas.models import Meta
from audio_src.apps.utils import constants


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, default='')
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(default='', blank=True)
    content = models.TextField(default='', blank=True)
    resource = models.TextField(null=True, blank=True)
    ping = models.BooleanField(default=True)
    type = models.IntegerField(
        choices=constants.post['TYPE_OPTIONS'], default=1)
    status = models.CharField(max_length=30, default='publish')
    isDeleted = models.BooleanField(default=False)
    thumbnail = models.URLField(default='', blank=True)
    # RelationShip
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    meta = models.OneToOneField(Meta, on_delete=models.SET_NULL, null=True)
    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
    # instance.info.delete()
    # def get_absolute_url(self):
    #     print("====>self.slug")
    #     print(self.slug)
    #     return reverse('article_detail_slug', kwargs={'slug': self.slug})

# Post.delete()
# class Post(models.Model):
#     content = models.TextField()
#     slug = models.SlugField(unique=True)
#     updated = models.DateTimeField(auto_now=True, auto_now_add=False)
#     timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

#     def __str__(self):
#         return self.content

#     class Meta:
#         ordering = ["timestamp", "updated"]
