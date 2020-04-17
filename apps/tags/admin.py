from django.contrib import admin
from tags.models import Tag

class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)
