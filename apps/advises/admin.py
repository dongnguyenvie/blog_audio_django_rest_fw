from django.contrib import admin
from advises.models import Advise


class AdvieAdmin(admin.ModelAdmin):
    pass


admin.site.register(Advise, AdvieAdmin)
