from django.contrib import admin
from audio_src.apps.tags.models import Tag

class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)
