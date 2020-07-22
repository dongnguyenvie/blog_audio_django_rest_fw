import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from audio_src.apps.blogs.models import Blog
from audio_src.apps.metas.models import Meta

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # RelationShip
    blog = models.OneToOneField(
        Blog, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.URLField(null=True, blank=True)
    meta = models.OneToOneField(Meta, on_delete=models.CASCADE, null=True, blank=True)

    # def __str__(self):
    #     return self.id
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
