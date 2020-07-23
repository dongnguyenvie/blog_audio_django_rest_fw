from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from audio_src.apps.users.models import CustomUser 
from audio_src.apps.users.forms import CustomUserChangeForm, CustomUserCreationForm
from django.utils.translation import gettext_lazy as _
# Register your models here.

class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = BaseUserAdmin.fieldsets + (
        (_('Extend fields'), {'fields': ('avatar', 'meta')},),
    )

admin.site.register(CustomUser, CustomUserAdmin)