from django.db import models

# Create your models here.


class Post(models.Model):
    content = models.TextField()
    slug = models.SlugField(unique=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    # def __str__(self):
    #     return self.content

# class Post(models.Model):
#     content = models.TextField()
#     slug = models.SlugField(unique=True)
#     updated = models.DateTimeField(auto_now=True, auto_now_add=False)
#     timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

#     def __str__(self):
#         return self.content

#     class Meta:
#         ordering = ["timestamp", "updated"]
