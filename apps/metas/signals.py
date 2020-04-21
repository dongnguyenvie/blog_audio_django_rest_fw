from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_save
from blogs.models import Blog
from metas.models import Meta
# @receiver(pre_save, sender=Blog)
# def post_save_ex(self, sender, instance, created, **kwargs):
#     pass
