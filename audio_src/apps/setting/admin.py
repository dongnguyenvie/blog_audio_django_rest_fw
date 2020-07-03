from django.contrib import admin
from audio_src.apps.setting.models import Setting


class SettingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Setting, SettingAdmin)
