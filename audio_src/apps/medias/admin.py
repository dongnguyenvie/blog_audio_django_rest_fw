from django.contrib import admin

from audio_src.apps.medias.models import Media


class MediaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Media, MediaAdmin)
