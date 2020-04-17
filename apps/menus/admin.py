from django.contrib import admin
from menus.models import Menu


class MenuAdmin(admin.ModelAdmin):
    pass


admin.site.register(Menu, MenuAdmin)
