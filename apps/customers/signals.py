from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group

MEMBER_GROUP = 'member'
@receiver(post_save, sender=User)
def add_to_default_group(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        group = Group.objects.get_or_create(name=MEMBER_GROUP)[0]
        user.groups.add(group.id)
