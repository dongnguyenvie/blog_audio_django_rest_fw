from django.contrib import admin
from audio_src.apps.menus.models import Menu


class MenuAdmin(admin.ModelAdmin):
    pass


admin.site.register(Menu, MenuAdmin)
