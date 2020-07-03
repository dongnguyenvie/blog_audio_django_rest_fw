from django.contrib import admin
from audio_src.apps.metas.models import Meta


class MetaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Meta, MetaAdmin)
