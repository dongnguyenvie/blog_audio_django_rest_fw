from django.contrib import admin
from setting.models import Setting


class SettingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Setting, SettingAdmin)
