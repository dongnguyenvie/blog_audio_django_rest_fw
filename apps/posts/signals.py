from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from posts.models import Post


@receiver(post_delete, sender=Post)
def auto_delete_publish_info_with_meta(sender, instance, **kwargs):
    try:
        instance.meta.delete()
    except:
        pass
