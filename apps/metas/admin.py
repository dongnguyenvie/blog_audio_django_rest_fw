from django.contrib import admin
from metas.models import Meta


class MetaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Meta, MetaAdmin)
