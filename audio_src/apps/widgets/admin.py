from django.contrib import admin
from audio_src.apps.widgets.models import Widget


class WidgetAdmin(admin.ModelAdmin):
    pass


admin.site.register(Widget, WidgetAdmin)
