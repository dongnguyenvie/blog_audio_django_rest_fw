from django.contrib import admin
from audio_src.apps.settings.models import Settings


class SettingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Settings, SettingAdmin)
